# This files contains your custom actions which can be used to run
# custom Python code.

import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Any, Text, Dict, List

import pandas
from geopy.geocoders import Nominatim
from rasa_sdk import Action, Tracker, logger
from rasa_sdk.events import SlotSet, UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction, REQUESTED_SLOT
from sqlalchemy import null

import zomato_api_query



def budget_extractor(budget):
	if budget == "0-300":
		min_price = 0
		max_price = 300
		return min_price, max_price
	elif budget == "301-700":
		min_price = 301
		max_price = 700
		return min_price, max_price
	else:
		min_price = 701
		max_price = 10000
		return min_price, max_price


class ActionSearchRestaurants(Action):
	
	def name(self) -> Text:
		return "action_search_restaurants"
	
	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
		# Initialize Zomato api
		config = {"user_key": "f5ca820b90f056a0f0c7f3f2ed17aeb2"}
		z = zomato_api_query.initialize_app(config=config)
		
		# Obtain slot values
		cuisine = tracker.get_slot('cuisine')
		budget = tracker.get_slot('budget')
		location = tracker.get_slot('location')
		
		if location != 'None':
			# Obtain geo-coordinate of the location
			geo_locator = Nominatim(user_agent="foodie_puff_bott")
			location_coord = geo_locator.geocode(location, country_codes="IN")
			
			# Latitude and Longitude
			lat = location_coord.latitude  # -> Float
			lon = location_coord.longitude  # -> Float
			
			# City id
			city_id = z.get_city_ID(location)  # city_id -> Int
			
			# Get dictionary with cuisines for city_id
			
			cuisine_master = z.get_cuisines(city_id)  # ->Dict
			cuisine_dict = {key: cuisine_master[key] for key in cuisine_master.keys() if
			                cuisine_master[key] == cuisine}  # -> Dict{code: cuisine}
			str_cuisine = list(cuisine_dict.keys())  # -> List[int]
			str_cuisine = [str(x) for x in str_cuisine]  # -> List[str]
			
			# Get restaurant id for cuisines
			rest_list = z.restaurant_search(latitude=lat, longitude=lon, cuisines=str_cuisine)  # -> List[str]
			
			# Obtain restaurant details from Zomato api get_restaurant method
			details_rest = []  # List of required restaurant details
			for i in rest_list:
				details_rest.append(z.get_restaurant(i))
			
			# Storing the required details in variables from the data obtained from the Zomato api
			name = []  # Name of the restaurants
			rating = []  # Aggregate ratings
			average_price = []  # Average Price for 2
			address = []  # Address
			
			# Populating the above variables
			for i in range(0, len(details_rest)):
				name.append(details_rest[i]['name'])
				address.append(details_rest[i]['location'])
				average_price.append(details_rest[i]['average_price'])
				rating.append(details_rest[i]['user_rating'])
			
			# Creating a pandas DataFrame of the above variables
			table = pandas.DataFrame({"name": name, "aggregate_rating": rating, "average_price": average_price,
			                          "address": address})
			
			# Extracting the indexes of those rows which meet the budget requirements
			rest_index = []  # List of indexes
			budget_range = budget_extractor(budget)  # Tuple of (min_price, max_price)
			for i in table.index:
				if table.loc[i, "average_price"] in range(budget_range[0], budget_range[1]):
					rest_index.append(i)
			
			# New DataFrame with the required restaurants
			table_new = table.loc[rest_index,]
			
			if len(list(table_new.name)) != 0:
				
				table_email = table_new.sort_values(axis=0, by='aggregate_rating', ascending=False).head(10)
				
				email_body = table_email.to_html()
				
				# Final table sorted by rating with top 5
				
				table_final = table_new.sort_values(axis=0, by='aggregate_rating', ascending=False).head(5)
				
				dispatcher.utter_message(text=f"Here are the names of the restaurants: {table_final} \n")
			
			else:
				email_body = []
				dispatcher.utter_message(text="Sorry couldn't find anything matching your specifications :(")
		else:
			email_body = []
			dispatcher.utter_template(tracker=tracker, template='utter_ask_location')
		
		if len(list(email_body)) != 0:
			
			return [SlotSet('email_body', email_body)]
		
		else:
			return []


class ActionSendEmail(Action):
	
	def name(self) -> Text:
		return "action_send_email"
	
	def run(
			self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
	) -> List[Dict[Text, Any]]:
		
		email_body = tracker.get_slot('email_body')
		user_mail = tracker.get_slot('email_address')
		bot_mail = "foodiebot3@gmail.com"
		bot_pass = "UpGrad123Bot!"
		context = ssl.create_default_context()
		msg = MIMEMultipart()
		
		message = """\
          <html>
         <head></head>
         <body>
           {0}
         </body>
         </html>
                 """.format(email_body)
		msg['Subject'] = "Top Restaurants matching your requirements"
		part1 = MIMEText(message, 'html')
		msg.attach(part1)
		
		try:
			server = smtplib.SMTP('smtp.gmail.com', 587)
			server.starttls(context=context)
			server.login(bot_mail, bot_pass)
			server.sendmail(bot_mail, user_mail, msg.as_string())
		except Exception as e:
			print(e)
		finally:
			server.quit()
		
		SlotSet('email_address', null)
		SlotSet('email_body', null)
		return []


class ActionCustomFallback(Action):
	
	def name(self) -> Text:
		return 'action_custom_fallback'
	
	async def run(
			self,
			dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any],
	) -> List[Dict[Text, Any]]:
		dispatcher.utter_message(template="utter_ask_rephrase")
		
		# Revert user message which led to fallback.
		return [UserUtteranceReverted()]


class RestaurantForm(FormAction):
	def name(self) -> Text:
		return "restaurant_form"  # Unique identifier of the form
	
	@staticmethod
	def required_slots(tracker: Tracker) -> List[Text]:
		# A list of required slots that the form has to fill
		return ["cuisine", "location", "budget"]
	
	def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
		# Define what the form has to do after all required slots are filled
		
		dispatcher.utter_message(template="utter_submit")
		return []
	
	def slot_mapping(self, dispatcher: CollectingDispatcher, tracker: Tracker):
		return {"cuisine": [self.from_entity(entity='cuisine', intent=['inform', 'restaurant_search']),
		                    self.from_entity(entity='PRODUCT')
		                    ],
		        "location": [self.from_entity(entity="location", intent=['restaurant_search', 'inform']),
		                     self.from_entity(entity='GPE'),
		                     ],
		        "budget": [self.from_entity(entity='budget', intent='inform'),
		                   self.from_intent(intent=['inform', 'restaurant_search'], value='budget')
		                   ]
		        }
	
	def validate_location(self, value, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
		cities_in_service = ["agra", "ajmer", "aligarh", "amravati", "amritsar", "asansol", "aurangabad",
		                     "bareilly",
		                     "belgaum", "bhavnagar", "bhiwandi", "bhopal", "bhubaneswar", "bikaner", "bilaspur",
		                     "bokaro steel city", "bokaro locality", "chandigarh", "coimbatore", "cuttack",
		                     "dehradun",
		                     "dhanbad",
		                     "bhilai", "durgapur", "dindigul", "erode", "faridabad", "firozabad", "ghaziabad",
		                     "gorakhpur", "gulbarga", "guntur", "gwalior", "gurgaon", "guwahati", "hamirpur",
		                     "hubli–dharwad", "indore", "jabalpur", "jaipur", "jalandhar", "jammu", "jamnagar",
		                     "jamshedpur", "jhansi", "jodhpur", "kakinada", "kannur", "kanpur", "karnal", "kochi",
		                     "kolhapur", "kollam", "kozhikode", "kurnool", "ludhiana", "lucknow", "madurai",
		                     "malappuram", "mathura", "mangalore", "meerut", "moradabad", "mysore", "nagpur",
		                     "nanded",
		                     "nashik", "nellore", "noida", "patna", "pondicherry", "purulia", "prayagraj", "raipur",
		                     "rajkot", "rajahmundry", "ranchi", "rourkela", "salem", "sangli", "shimla", "siliguri",
		                     "solapur", "srinagar", "surat", "thanjavur", "thiruvananthapuram", "thrissur",
		                     "tiruchirappalli", "tirunelveli", "ujjain", "bijapur", "vadodara", "varanasi",
		                     "vasai-virarcity", "vijayawada", "visakhapatnam", "vellore", "warangal", "ahmedabad",
		                     "bengaluru", "chennai", "delhi ncr", "hyderabad", "kolkata", "mumbai", "pune"]
		
		if value.lower() in cities_in_service:
			loc = value.lower()
			return {'location': loc}
		else:
			# dispatcher.utter_message(template="utter_not_in_loc", tracker=tracker)
			# validation failed, set this slot to None, meaning the
			# user will be asked for the slot again
			dispatcher.utter_message(template='utter_confirm_loc')
			return {'location': None}
	
	def validate_cuisine(self, value, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
		cuisines = ['chinese', 'north indian', 'mexican', 'south indian', 'american', 'italian']
		if value.lower() in cuisines:
			return {'cuisine': value.lower()}
		else:
			dispatcher.utter_message(template='utter_confirm_cuisine')
			
			return {'cuisine': None}
	
	def validate_budget(self, value, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
		budget = ['0-300', '301-700', '700 above']
		if value.lower() in budget:
			return {'budget': value.lower()}
		else:
			dispatcher.utter_message(template='utter_confirm_budget')
		
		return {'budget': None}
	
	def request_next_slot(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
		
		for slot in self.required_slots(tracker):
			if self._should_request_slot(tracker, slot):
				logger.debug(f"Request next slot '{slot}'")
				dispatcher.utter_message(template=f"utter_ask_{slot}", **tracker.slots)
				return [SlotSet(REQUESTED_SLOT, slot)]
		
		return None


class ActionCheckCuisine(Action):
	
	def name(self) -> Text:
		return "action_check_cuisine"
	
	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
		cuisines = ['chinese', 'north indian', 'mexican', 'south indian', 'american', 'italian']
		
		cui = tracker.get_slot('cuisine')
		cui = cui.lower()  # Converting to lowercase
		if cui in cuisines:
			SlotSet('cuisine', cui)
			return []
		else:
			dispatcher.utter_message(template='utter_confirm_cuisine')
			SlotSet('cuisine', null)
			return []


class ActionCheckBudget(Action):
	
	def name(self) -> Text:
		return "action_check_budget"
	
	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
		budget = ['0-300', '301-700', '700 above']
		
		bug = tracker.get_slot('budget')
		bug = bug.lower()  # Converting to lowercase
		if bug in budget:
			SlotSet('budget', bug)
			return []
		else:
			dispatcher.utter_message(template='utter_confirm_budget')
			SlotSet('budget', null)
			return []


class ActionCheckLocation(Action):
	
	def name(self) -> Text:
		return "action_check_location"
	
	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
		# Getting the location from the tracker file
		loc = tracker.get_slot('location')
		loc = loc.lower()  # Converting to lowercase
		# List of all tier_1 and tier_2 cities
		cities_in_service = ["agra", "ajmer", "aligarh", "amravati", "amritsar", "asansol", "aurangabad", "bareilly",
		                     "belgaum", "bhavnagar", "bhiwandi", "bhopal", "bhubaneswar", "bikaner", "bilaspur",
		                     "bokaro locality", "chandigarh", "coimbatore", "cuttack", "dehradun",
		                     "dhanbad",
		                     "bhilai", "durgapur", "dindigul", "erode", "faridabad", "firozabad", "ghaziabad",
		                     "gorakhpur", "gulbarga", "guntur", "gwalior", "gurgaon", "guwahati", "hamirpur",
		                     "hubli–dharwad", "indore", "jabalpur", "jaipur", "jalandhar", "jammu", "jamnagar",
		                     "jamshedpur", "jhansi", "jodhpur", "kakinada", "kannur", "kanpur", "karnal", "kochi",
		                     "kolhapur", "kollam", "kozhikode", "kurnool", "ludhiana", "lucknow", "madurai",
		                     "malappuram", "mathura", "mangalore", "meerut", "moradabad", "mysore", "nagpur", "nanded",
		                     "nashik", "nellore", "noida", "patna", "pondicherry", "purulia", "prayagraj", "raipur",
		                     "rajkot", "rajahmundry", "ranchi", "rourkela", "salem", "sangli", "shimla", "siliguri",
		                     "solapur", "srinagar", "surat", "thanjavur", "thiruvananthapuram", "thrissur",
		                     "tiruchirappalli", "tirunelveli", "ujjain", "bijapur", "vadodara", "varanasi",
		                     "vasai-virarcity", "vijayawada", "visakhapatnam", "vellore", "warangal", "ahmedabad",
		                     "bengaluru", "chennai", "delhi ncr", "hyderabad", "kolkata", "mumbai", "pune"]
		
		# Setting slot 'location'
		if not (loc in cities_in_service):
			
			dispatcher.utter_message(template='utter_confirm_loc')
			SlotSet('location', null)
			return []
		else:
			SlotSet('location', loc)
			return []
