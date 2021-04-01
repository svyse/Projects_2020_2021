## happy path
* restaurant_search
   - restaurant_form
   - form{"name": "restaurant_form"}
   - form{"name": null}
   
   
   

## interactive_story_1
* restaurant_search
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "cuisine"}
* form: inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - form: restaurant_form
    - slot{"cuisine": "chinese"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Mumbai", "GPE": "Mumbai"}
    - slot{"location": "Mumbai"}
    - form: restaurant_form
    - slot{"location": "mumbai"}
    - slot{"requested_slot": "budget"}
* form: inform{"budget": "700"}
    - slot{"budget": "700"}
    - form: restaurant_form
    - slot{"budget": ["301 700"]}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"email_body": "<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>name</th>\n      <th>aggregate_rating</th>\n      <th>average_price</th>\n      <th>address</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>Mirchi And Mime</td>\n      <td>4.9</td>\n      <td>1800</td>\n      <td>G6,One Boulevard,Lake Boulevard Road, Hiranandani Business Park, Powai, Mumbai</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>Pa Pa Ya</td>\n      <td>4.9</td>\n      <td>2000</td>\n      <td>Palladium Mall, Level 3, Senapati Bapat Marg, Lower Parel, Mumbai</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>Shree Thaker Bhojanalay</td>\n      <td>4.9</td>\n      <td>1300</td>\n      <td>31, Dadisheth Agyari Lane, Off Kalbadevi Road, Kalbadevi, Mumbai</td>\n    </tr>\n    <tr>\n      <th>6</th>\n      <td>Peshawri - ITC Maratha</td>\n      <td>4.9</td>\n      <td>5000</td>\n      <td>ITC Maratha, Sahar Road, Chakala, Mumbai</td>\n    </tr>\n    <tr>\n      <th>7</th>\n      <td>Bayroute</td>\n      <td>4.9</td>\n      <td>3000</td>\n      <td>1, Ground Floor, Transocean House, Lake Blve Road, Hiranandani Business Park, Powai, Mumbai</td>\n    </tr>\n    <tr>\n      <th>10</th>\n      <td>Bastian</td>\n      <td>4.8</td>\n      <td>4200</td>\n      <td>B/1, New Kamal Building, Opposite National College, Linking Road, Bandra West, Mumbai</td>\n    </tr>\n    <tr>\n      <th>11</th>\n      <td>Masala Library</td>\n      <td>4.8</td>\n      <td>3500</td>\n      <td>Ground Floor, First International Financial Centre, Bandra Kurla Complex, Mumbai</td>\n    </tr>\n    <tr>\n      <th>13</th>\n      <td>JW Café - JW Marriott Mumbai Sahar</td>\n      <td>4.8</td>\n      <td>4000</td>\n      <td>IA Project Road, Chhatrapati Shivaji International Airport, Chakala, Mumbai</td>\n    </tr>\n    <tr>\n      <th>18</th>\n      <td>Aer - Four Seasons</td>\n      <td>4.7</td>\n      <td>4500</td>\n      <td>1/136, E Moses Road, Worli, Mumbai</td>\n    </tr>\n    <tr>\n      <th>19</th>\n      <td>Hakkasan</td>\n      <td>4.7</td>\n      <td>2600</td>\n      <td>206, 2nd Floor, Krystal, Waterfield Road, Linking Road, Bandra West, Mumbai</td>\n    </tr>\n  </tbody>\n</table>"}
    - utter_ask_email
* affirm
    - utter_enter_email
* inform{"email_address": "sherardv@live.com"}
    - slot{"email_address": "sherardv@live.com"}
    - action_send_email
    - utter_sent_email
* goodbye
    - utter_goodbye

## interactive_story_2
* greet
    - utter_greet
* restaurant_search
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "cuisine"}
* form: inform{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - form: restaurant_form
    - slot{"cuisine": "mexican"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - form: restaurant_form
    - slot{"location": "jaipur"}
    - slot{"requested_slot": "budget"}
* form: inform{"budget": "700"}
    - slot{"budget": "700"}
    - form: restaurant_form
    - slot{"budget": "700"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"email_body": "<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>name</th>\n      <th>aggregate_rating</th>\n      <th>average_price</th>\n      <th>address</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>Steam - Rambagh Palace</td>\n      <td>4.8</td>\n      <td>2800</td>\n      <td>Rambagh Palace, Bhawani Singh Road, C Scheme, Jaipur</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>Tapri Central</td>\n      <td>4.7</td>\n      <td>800</td>\n      <td>B4 E, 3rd Floor, Surana Jewellers, Opposite Central Park, C Scheme, Jaipur</td>\n    </tr>\n    <tr>\n      <th>6</th>\n      <td>The Night Jar</td>\n      <td>4.6</td>\n      <td>1200</td>\n      <td>3rd Floor, Panch Batti, MI Road, Jaipur</td>\n    </tr>\n    <tr>\n      <th>7</th>\n      <td>Farzi Cafe</td>\n      <td>4.6</td>\n      <td>2000</td>\n      <td>Radisson Jaipur City Center, Khasa Kothi Circle, MI Road, Jaipur</td>\n    </tr>\n    <tr>\n      <th>9</th>\n      <td>Okra - Jaipur Marriott Hotel</td>\n      <td>4.6</td>\n      <td>2600</td>\n      <td>Jaipur Marriott Hotel, Ashram Marg, Near Jawahar Circle, Durgapura, Jaipur</td>\n    </tr>\n    <tr>\n      <th>10</th>\n      <td>Peshawri - ITC Rajputana Hotel</td>\n      <td>4.6</td>\n      <td>3000</td>\n      <td>ITC Rajputana Hotel, Palace Road, Gopalbari, Jaipur</td>\n    </tr>\n    <tr>\n      <th>13</th>\n      <td>Café Bae</td>\n      <td>4.5</td>\n      <td>1200</td>\n      <td>A1, 21 Sehkar Marg, Bais Godam, Jaipur</td>\n    </tr>\n    <tr>\n      <th>14</th>\n      <td>Jaipur Adda</td>\n      <td>4.5</td>\n      <td>1600</td>\n      <td>Nirwana Hometel, 4 D Villa, Khasa Kothi Circle, Station Road, Bani Park, Jaipur</td>\n    </tr>\n    <tr>\n      <th>15</th>\n      <td>Chokhi Dhani</td>\n      <td>4.5</td>\n      <td>1800</td>\n      <td>Chokhi Dhani Village Resort, 12 Mile, Sitapur, Jaipur</td>\n    </tr>\n    <tr>\n      <th>16</th>\n      <td>OTB - On The Bar B-Q</td>\n      <td>4.5</td>\n      <td>1200</td>\n      <td>6th Floor, Crystal Court Mall, Malviya Nagar, Jaipur</td>\n    </tr>\n  </tbody>\n</table>"}
    - utter_ask_email
* affirm
    - utter_enter_email
* inform{"email_address": "sherardv@live.com"}
    - slot{"email_address": "sherardv@live.com"}
    - action_send_email
    - utter_sent_email
* goodbye
    - utter_goodbye

## interactive_story_3
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_check_cuisine
    - slot{"cuisine": "South Indian"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"cuisine": "South Indian"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Bhopal"}
    - slot{"location": "Bhopal"}
    - form: restaurant_form
    - slot{"location": "bhopal"}
    - slot{"requested_slot": "budget"}
* form: inform{"budget": "700"}
    - slot{"budget": "700"}
    - form: restaurant_form
    - slot{"budget": ["301- 700"]}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"email_body": "<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>name</th>\n      <th>aggregate_rating</th>\n      <th>average_price</th>\n      <th>address</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>1</th>\n      <td>Shahnama - Jehan Numa Palace</td>\n      <td>4.6</td>\n      <td>2000</td>\n      <td>Hotel Jehan Numa Palace, 157, Shymala Hills, TT Nagar, Bhopal</td>\n    </tr>\n  </tbody>\n</table>"}
    - utter_ask_email
* deny
    - utter_goodbye

## interactive_story_4
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Sihora"}
    - slot{"location": "Sihora"}
    - form: restaurant_form
    - slot{"location": "Sihora"}
    - slot{"requested_slot": null}
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_goodbye

## interactive_story_5
* restaurant_search
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "cuisine"}
* form: inform{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - form: restaurant_form
    - slot{"cuisine": "italian"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Mawanagar"}
    - slot{"location": "Mawanagar"}
    - form: restaurant_form
    - slot{"location": "Mawanagar"}
    - slot{"requested_slot": "budget"}
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_goodbye
* goodbye

## interactive_story_6
* restaurant_search
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "cuisine"}
* form: inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - form: restaurant_form
    - slot{"cuisine": "chinese"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "jabalpur"}
    - slot{"location": "jabalpur"}
    - form: restaurant_form
    - slot{"location": "jabalpur"}
    - slot{"requested_slot": "budget"}
* form: inform{"budget": "301-700"}
    - slot{"budget": "301-700"}
    - form: restaurant_form
    - slot{"budget": "301-700"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"email_body": "<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>name</th>\n      <th>aggregate_rating</th>\n      <th>average_price</th>\n      <th>address</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>1</th>\n      <td>Domino's Pizza</td>\n      <td>4.5</td>\n      <td>400</td>\n      <td>Plot 128 &amp; 129, Ground Floor, Laxmi Pur, Vijay Nagar, Jabalpur</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>The Belgian Waffle Co.</td>\n      <td>4.5</td>\n      <td>350</td>\n      <td>Shop 13, Civic Center, Near Bata Showroom, Marhatal, Jabalpur</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>Domino's Pizza</td>\n      <td>4.4</td>\n      <td>400</td>\n      <td>Block 4, Russell Crossing, Near Jyoti Talkies, Napier Town, Jabalpur</td>\n    </tr>\n    <tr>\n      <th>8</th>\n      <td>Desi Twist</td>\n      <td>4.4</td>\n      <td>400</td>\n      <td>Near Ridge Road Entrance, Denning Road, South Civil Lines, Jabalpur</td>\n    </tr>\n    <tr>\n      <th>9</th>\n      <td>Indian Coffee House</td>\n      <td>4.4</td>\n      <td>600</td>\n      <td>Sadar, Cantt, Jabalpur</td>\n    </tr>\n    <tr>\n      <th>11</th>\n      <td>New Pawar Restaurant</td>\n      <td>4.3</td>\n      <td>600</td>\n      <td>Near Old Bus Stand, Model Road, Wright Town, Jabalpur</td>\n    </tr>\n    <tr>\n      <th>15</th>\n      <td>KFC</td>\n      <td>4.3</td>\n      <td>450</td>\n      <td>Shop 1, 2, 3, 4 &amp; 5, First Floor &amp; Ground Floor, South Avenue Mall, Narmada Road, Rampur, Jabalpur</td>\n    </tr>\n    <tr>\n      <th>16</th>\n      <td>The Cake Company</td>\n      <td>4.3</td>\n      <td>400</td>\n      <td>Besides Oven Classics, Civil Lines, Civil Lines, Jabalpur</td>\n    </tr>\n  </tbody>\n</table>"}
    - utter_ask_email
* affirm
    - utter_enter_email
* inform{"email_address": "sherardv@live.com"}
    - slot{"email_address": "sherardv@live.com"}
    - action_send_email
    - utter_sent_email
* goodbye
    - utter_goodbye

## interactive_story_7
* greet
    - utter_greet
* restaurant_search
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "cuisine"}
* form: inform{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - form: restaurant_form
    - slot{"cuisine": "mexican"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "turbinenagar"}
    - slot{"location": "turbinenagar"}
    - form: restaurant_form
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* affirm
    - utter_not_in_loc
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_goodbye
* affirm

## interactive_story_8
* restaurant_search{"location": "turbinenagar"}
    - slot{"location": "turbinenagar"}
    - action_check_location
    - slot{"location": null}
    - utter_not_in_loc
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_9
* greet
    - utter_greet
* restaurant_search{"cuisine": "korean", "location": "mumbai"}
    - slot{"cuisine": "korean"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - action_check_cuisine
    - slot{"cuisine": null}
    - utter_ask_cuisine
* inform{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* inform{"budget": "301-700"}
    - slot{"budget": "301-700"}
    - action_search_restaurants
    - slot{"email_body": "<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>name</th>\n      <th>aggregate_rating</th>\n      <th>average_price</th>\n      <th>address</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>5</th>\n      <td>A.Rama Nayak's Udipi Shri Krishna Boarding</td>\n      <td>4.8</td>\n      <td>400</td>\n      <td>1st Floor, LBS Market Building, Near Matunga Central Railway Station, Matunga East, Mumbai</td>\n    </tr>\n    <tr>\n      <th>9</th>\n      <td>Vinay Health Home</td>\n      <td>4.7</td>\n      <td>400</td>\n      <td>Jawar Mansion, Dr BA Jaikar Marg, Charni Road, Mumbai</td>\n    </tr>\n    <tr>\n      <th>18</th>\n      <td>Hotel Shankar Palace</td>\n      <td>4.5</td>\n      <td>350</td>\n      <td>Shop 52, Prabhat Center, Sector 6, Near CBD-Belapur, Navi Mumbai</td>\n    </tr>\n  </tbody>\n</table>"}
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart

## interactive_story_10
* restaurant_search{"location": "kalyan"}
    - slot{"location": "kalyan"}
    - action_check_location
    - slot{"location": null}
    - utter_ask_location
* inform{"location": "visakhapatnam"}
    - slot{"location": "visakhapatnam"}
    - action_check_location
    - slot{"location": "visakhapatnam"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "visakhapatnam"}
    - slot{"location": "visakhapatnam"}
    - slot{"requested_slot": "cuisine"}
* form: inform{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - form: restaurant_form
    - slot{"cuisine": "italian"}
    - slot{"requested_slot": "budget"}
* form: inform{"budget": "700 above"}
    - slot{"budget": "700 above"}
    - form: restaurant_form
    - slot{"budget": "700 above"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"email_body": "<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>name</th>\n      <th>aggregate_rating</th>\n      <th>average_price</th>\n      <th>address</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>AB's - Absolute Barbecue</td>\n      <td>4.7</td>\n      <td>1250</td>\n      <td>4th Floor, Plot 244A, Uma Vinayagar, Dwaraka Nagar, Vizag</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>Flying Spaghetti Monster</td>\n      <td>4.7</td>\n      <td>1400</td>\n      <td>10-50-12/F2, Sai Dakshata Complex, Beside Lenovo Showroom,   Visakhapatnam, Waltair Uplands, Waltair Uplands, Vizag</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>Upland Bistro</td>\n      <td>4.5</td>\n      <td>1200</td>\n      <td>sai dakshita complex, 10-50-12/3,first floor, Waltair uplands,Waltair Main Road,Visakhapatnam, Andhra Pradesh 530003 India</td>\n    </tr>\n    <tr>\n      <th>7</th>\n      <td>Kamat Restaurant</td>\n      <td>4.4</td>\n      <td>800</td>\n      <td>Beach Road, Near Santhi Ashram, Lawsons Bay, Visakhapatnam</td>\n    </tr>\n    <tr>\n      <th>9</th>\n      <td>Zeeshan Restaurant - Apna Hyderabadi Food</td>\n      <td>4.4</td>\n      <td>900</td>\n      <td>28-10-3, Ground Floor, Opposite Chitralaya Mall, Jagadamba Junction, Vizag</td>\n    </tr>\n    <tr>\n      <th>12</th>\n      <td>Mekong - Hotel GreenPark</td>\n      <td>4.4</td>\n      <td>1300</td>\n      <td>Hotel GreenPark, Waltair Main Road, Waltair Uplands, Vizag</td>\n    </tr>\n    <tr>\n      <th>17</th>\n      <td>The Spicy Venue</td>\n      <td>4.4</td>\n      <td>900</td>\n      <td>27, 9-30-2/1, Balaji Nagar, Siripuram, Vizag</td>\n    </tr>\n  </tbody>\n</table>"}
    - utter_ask_email
* affirm
    - utter_enter_email
* inform{"email_address": "hiranya.22.singh@gmail.com"}
    - slot{"email_address": "hiranya.22.singh@gmail.com"}
    - action_send_email
    - utter_sent_email
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_11
    - utter_greet
* restaurant_search
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "cuisine"}
* form: inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - form: restaurant_form
    - slot{"cuisine": "chinese"}
    - slot{"requested_slot": "location"}
* inform{"GPE": "america"}
    - utter_not_in_loc
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_goodbye

## interactive_story_12
* restaurant_search{"location": "zimbabwe"}
    - slot{"location": "zimbabwe"}
    - action_check_location
    - slot{"location": null}
    - utter_ask_location
    - utter_not_in_loc
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_13
    - utter_greet
* restaurant_search{"cuisine": "continental", "location": "South Africa"}
    - slot{"cuisine": "continental"}
    - slot{"location": "South Africa"}
    - action_check_location
    - slot{"location": null}
    - utter_not_in_loc
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_14
    - utter_greet
* restaurant_search{"cuisine": "italian", "budget": "500 rs"}
    - slot{"budget": "500 rs"}
    - slot{"cuisine": "italian"}
    - action_check_budget
    - utter_ask_budget
* inform{"budget": "700 above"}
    - slot{"budget": "700 above"}
    - utter_ask_location
* inform{"location": "jodhpur"}
    - slot{"location": "jodhpur"}
    - action_check_location
    - slot{"location": "jodhpur"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"cuisine": "italian"}
    - slot{"location": "jodhpur"}
    - slot{"budget": null}
    - slot{"location": "jodhpur"}
    - slot{"requested_slot": "budget"}
* form: inform{"budget": "700 above"}
    - slot{"budget": "700 above"}
    - form: restaurant_form
    - slot{"budget": "700 above"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"email_body": "<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>name</th>\n      <th>aggregate_rating</th>\n      <th>average_price</th>\n      <th>address</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>1</th>\n      <td>Khaas Bagh</td>\n      <td>4.7</td>\n      <td>1500</td>\n      <td>Opposite Police Lines, Ratanada, Bhagat Ki Kothi, Jodhpur</td>\n    </tr>\n    <tr>\n      <th>7</th>\n      <td>Cafe 651</td>\n      <td>4.5</td>\n      <td>850</td>\n      <td>651, 11th C Road, Sardarpura, Bhagat Ki Kothi, Jodhpur</td>\n    </tr>\n  </tbody>\n</table>"}
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart

## interactive_story_15
    - action_default_ask_rephrase
* out_of_scope
    - utter_out_of_scope
* chitchat
    - utter_goodbye

## interactive_story_16
* restaurant_search{"location": "meghalaya"}
    - slot{"location": "meghalaya"}
    - action_check_location
    - slot{"location": null}
    - utter_confirm_loc
* affirm
    - utter_not_in_loc
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_17
    - utter_greet
* out_of_scope
    - utter_out_of_scope
* out_of_scope
    - utter_out_of_scope
    - utter_goodbye
    - action_restart

## interactive_story_18
* chitchat{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - utter_chitchat
* chitchat
    - utter_out_of_scope
    - utter_goodbye
    - action_restart

## interactive_story_19
* greet
    - utter_greet
* wellbeing
    - utter_wellbeing
* out_of_scope
    - utter_out_of_scope
    - utter_goodbye
    - action_restart

## interactive_story_20
    - utter_greet
* wellbeing
    - utter_wellbeing
* restaurant_search{"location": "Rajasthan"}
    - slot{"location": "Rajasthan"}
    - action_check_location
    - slot{"location": null}
    - utter_confirm_loc
* inform{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - action_check_location
    - slot{"location": "jaipur"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "jaipur"}
    - slot{"requested_slot": "cuisine"}
* form: inform{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - form: restaurant_form
    - slot{"cuisine": "american"}
    - slot{"requested_slot": "budget"}
* form: inform{"budget": "300-700"}
    - slot{"budget": "300-700"}
    - form: restaurant_form
    - slot{"budget": null}
    - slot{"requested_slot": "budget"}
* form: inform{"budget": "301-700"}
    - slot{"budget": "301-700"}
    - form: restaurant_form
    - slot{"budget": "301-700"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"email_body": "<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>name</th>\n      <th>aggregate_rating</th>\n      <th>average_price</th>\n      <th>address</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>2</th>\n      <td>Curious Life Coffee Roasters- Sarojini Marg</td>\n      <td>4.7</td>\n      <td>600</td>\n      <td>C 54 A, Sarojini Marg, C Scheme, Jaipur</td>\n    </tr>\n    <tr>\n      <th>15</th>\n      <td>Anokhi Cafe</td>\n      <td>4.5</td>\n      <td>550</td>\n      <td>C 11, 2nd Floor, KK Square, C Scheme, Jaipur</td>\n    </tr>\n    <tr>\n      <th>16</th>\n      <td>Jal Mahal Ice Cream Parlour</td>\n      <td>4.5</td>\n      <td>400</td>\n      <td>85, MI Road, Jaipur</td>\n    </tr>\n  </tbody>\n</table>"}
    - utter_ask_email
* deny
    - utter_goodbye

## interactive_story_21
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_check_cuisine
    - slot{"cuisine": "south indian"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "kumaohabad"}
    - slot{"location": "kumaohabad"}
    - form: restaurant_form
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* affirm
    - utter_not_in_loc
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_goodbye

## interactive_story_22
* greet
    - utter_greet
* chitchat{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - action_check_location
    - slot{"location": "hyderabad"}
    - utter_chitchat
* chitchat
    - utter_chitchat
    - utter_out_of_scope
    - utter_goodbye
    - action_restart

## interactive_story_23
* out_of_scope
    - utter_out_of_scope
* out_of_scope
    - utter_out_of_scope
    - utter_goodbye
    - action_restart

## interactive_story_24
    - utter_greet
* restaurant_search{"budget": "900"}
    - slot{"budget": "900"}
    - action_check_budget
    - utter_ask_budget
* inform{"budget": "700 above"}
    - slot{"budget": "700 above"}
    - utter_ask_location
* inform{"location": "ahemdabad"}
    - slot{"location": "ahemdabad"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": null}
    - slot{"budget": "700 above"}
    - slot{"location": null}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - form: restaurant_form
    - slot{"cuisine": "italian"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "ahemdabad"}
    - slot{"location": "ahemdabad"}
    - form: restaurant_form
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* form: inform{"location": "ahmedabad"}
    - slot{"location": "ahmedabad"}
    - form: restaurant_form
    - slot{"location": "ahmedabad"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"email_body": "<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>name</th>\n      <th>aggregate_rating</th>\n      <th>average_price</th>\n      <th>address</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>1</th>\n      <td>Dravida - The Fern</td>\n      <td>4.9</td>\n      <td>1600</td>\n      <td>Near Sola Overbridge, SG Highway, Sola, Ahmedabad</td>\n    </tr>\n    <tr>\n      <th>9</th>\n      <td>The Red Bistro</td>\n      <td>4.6</td>\n      <td>1400</td>\n      <td>Armeida, Sindhu Bhavan Road, Off SG Road, Near Bodakdev, Ahmedabad</td>\n    </tr>\n    <tr>\n      <th>10</th>\n      <td>Rajwadu</td>\n      <td>4.6</td>\n      <td>1300</td>\n      <td>Near Jivraj Tolnaka, Ambaji Temple, Malav Talav, Vejalpur, Ahmedabad</td>\n    </tr>\n    <tr>\n      <th>14</th>\n      <td>TG’s - The Oriental Grill - Hyatt</td>\n      <td>4.6</td>\n      <td>2200</td>\n      <td>Near Vastrapur Lake, Vastrapur, Ahmedabad</td>\n    </tr>\n    <tr>\n      <th>19</th>\n      <td>Lollo Rosso</td>\n      <td>4.5</td>\n      <td>900</td>\n      <td>Shop 2, Ground Floor, Aeon Complex, Opposite Navkar Institute, Navrangpura, Ahmedabad</td>\n    </tr>\n  </tbody>\n</table>"}
    - utter_ask_email
* affirm
    - utter_enter_email
* inform{"email_address": "mjvyse@gmail.com"}
    - slot{"email_address": "mjvyse@gmail.com"}
    - action_send_email
    - utter_sent_email
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_25
    - utter_greet
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "guntur"}
    - slot{"location": "guntur"}
    - form: restaurant_form
    - slot{"location": "guntur"}
    - slot{"requested_slot": "budget"}
* form: inform{"budget": "0-300"}
    - slot{"budget": "0-300"}
    - form: restaurant_form
    - slot{"budget": "0-300"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"email_body": "<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>name</th>\n      <th>aggregate_rating</th>\n      <th>average_price</th>\n      <th>address</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>Varalakshmi Tiffins</td>\n      <td>4.5</td>\n      <td>200</td>\n      <td>Near Seetharamayya High School, 6th Line, Lakshmipuram Main Road, Chandramouli Nagar, Lakshmipuram, Guntur</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>Raja Tiffins And Meals</td>\n      <td>4.5</td>\n      <td>150</td>\n      <td>Old 5-42-41, New 30-02-336, 6/13, Brodipet, Guntur</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>House Of Bakers</td>\n      <td>4.5</td>\n      <td>200</td>\n      <td>Door 5-72-62, 1st Lane, Pandaripuram, Lakshmipuram, Guntur</td>\n    </tr>\n    <tr>\n      <th>6</th>\n      <td>Vijaya Cool Drinks</td>\n      <td>4.4</td>\n      <td>200</td>\n      <td>NTR Stadium Complex, Brundavan Gardens, Main Road, Laxmipuram, Lakshmipuram, Guntur</td>\n    </tr>\n  </tbody>\n</table>"}
    - utter_ask_email
* affirm
    - utter_enter_email
* inform{"email_address": "sherardv@live.com"}
    - slot{"email_address": "sherardv@live.com"}
    - action_send_email
    - utter_sent_email
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_26
    - utter_greet
* restaurant_search{"location": "cuttack"}
    - slot{"location": "cuttack"}
    - action_check_location
    - slot{"location": "cuttack"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "cuttack"}
    - slot{"requested_slot": "cuisine"}
* form: inform{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - form: restaurant_form
    - slot{"cuisine": "north indian"}
    - slot{"requested_slot": "budget"}
* form: inform{"budget": "301-700"}
    - slot{"budget": "301-700"}
    - form: restaurant_form
    - slot{"budget": "301-700"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"email_body": "<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>name</th>\n      <th>aggregate_rating</th>\n      <th>average_price</th>\n      <th>address</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>Ice - Indian Chicken Express</td>\n      <td>4.9</td>\n      <td>350</td>\n      <td>Rex Plaza, College Sqaure, Siba Bazaar, Cuttack</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>Domino's Pizza</td>\n      <td>4.4</td>\n      <td>400</td>\n      <td>Rex Plaza, College Square, Siba Bazaar, Cuttack</td>\n    </tr>\n    <tr>\n      <th>6</th>\n      <td>DFC Dada's Biryani</td>\n      <td>4.4</td>\n      <td>400</td>\n      <td>Near UCO Bank, YMCA, Cuttack</td>\n    </tr>\n    <tr>\n      <th>7</th>\n      <td>Blast</td>\n      <td>4.4</td>\n      <td>500</td>\n      <td>TOP FLOOR, REX PLAZA, COLLEGE SQUARE</td>\n    </tr>\n    <tr>\n      <th>8</th>\n      <td>ICE- Indian Chicken Express</td>\n      <td>4.4</td>\n      <td>350</td>\n      <td>Indian chicken express.NSCB Arcade.shop no 2&amp; 28. dargha bazar .buxi bazar .Cuttack</td>\n    </tr>\n    <tr>\n      <th>9</th>\n      <td>WOW! Momo</td>\n      <td>4.4</td>\n      <td>350</td>\n      <td>Beside Sangam Complex, Mahatab Road, Bajrakabati, Mal Godown Market, Cuttack</td>\n    </tr>\n    <tr>\n      <th>12</th>\n      <td>KFC</td>\n      <td>4.3</td>\n      <td>450</td>\n      <td>1360 &amp; 1361, Unit -35, Jhanjir Mangala, Cuttack, Ward -29, Cuttack Municipal Corporation</td>\n    </tr>\n    <tr>\n      <th>15</th>\n      <td>Baker's Delite</td>\n      <td>4.3</td>\n      <td>400</td>\n      <td>Near SB Women College, Biju Patnaik Colony, Buxi Bazaar, Cuttack</td>\n    </tr>\n    <tr>\n      <th>16</th>\n      <td>Biggies Burger</td>\n      <td>4.2</td>\n      <td>600</td>\n      <td>College Square, Beside Kitab Mahal, Cuttack</td>\n    </tr>\n    <tr>\n      <th>17</th>\n      <td>Mirchi</td>\n      <td>4.2</td>\n      <td>500</td>\n      <td>Shop 22, J.P Market, Buxibazar, Cuttack</td>\n    </tr>\n  </tbody>\n</table>"}
    - utter_ask_email
* deny
    - utter_goodbye
* goodbye

## interactive_story_27
* greet
    - utter_greet
* out_of_scope
    - utter_out_of_scope
* restaurant_search{"GPE": "delhi", "location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "delhi"}
    - slot{"requested_slot": "cuisine"}
* form: inform{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - form: restaurant_form
    - slot{"cuisine": "american"}
    - slot{"requested_slot": "budget"}
* inform{"budget": "5"}
    - slot{"budget": "5"}
    - action_check_budget
    - utter_ask_budget
* inform{"budget": "700 above"}
    - slot{"budget": "700 above"}
    - restaurant_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - utter_ask_email
* deny
    - utter_goodbye

## interactive_story_28
* out_of_scope
    - utter_out_of_scope
* chitchat
    - utter_chitchat
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "delhi"}
    - slot{"requested_slot": "cuisine"}
* form: inform{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - form: restaurant_form
    - slot{"cuisine": "south indian"}
    - slot{"requested_slot": "budget"}
* form: inform{"budget": "700 above"}
    - slot{"budget": "700 above"}
    - form: restaurant_form
    - slot{"budget": "700 above"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - utter_ask_email
* deny
    - utter_goodbye
* goodbye

## interactive_story_29
* restaurant_search{"location": "delhi ncr"}
    - slot{"location": "delhi ncr"}
    - action_check_location
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "delhi ncr"}
    - slot{"requested_slot": "cuisine"}
* form: inform{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - form: restaurant_form
    - slot{"cuisine": "mexican"}
    - slot{"requested_slot": "budget"}
* form: inform{"budget": "301-700"}
    - slot{"budget": "301-700"}
    - form: restaurant_form
    - slot{"budget": "301-700"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - utter_ask_email
* deny
    - utter_goodbye
* goodbye

## interactive_story_1
* restaurant_search
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "cuisine"}
* form: inform{"cuisine": "japanese"}
    - slot{"cuisine": "japanese"}
    - form: restaurant_form
    - slot{"cuisine": null}
    - slot{"requested_slot": "cuisine"}
* form: inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - form: restaurant_form
    - slot{"cuisine": "chinese"}
    - slot{"requested_slot": "location"}
* chitchat
    - utter_chitchat
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_location
* out_of_scope
    - utter_out_of_scope
* inform{"GPE": "Nagpur", "location": "Nagpur"}
    - slot{"location": "Nagpur"}
    - action_check_location
    - restaurant_form
    - form{"name": "restaurant_form"}
    - action_listen
    - slot{"cuisine": "chinese"}
    - slot{"location": "nagpur"}
    - slot{"requested_slot": "budget"}
* form: inform{"budget": "301-700"}
    - slot{"budget": "301-700"}
    - restaurant_form
    - slot{"budget": "301-700"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"email_body": "<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>name</th>\n      <th>aggregate_rating</th>\n      <th>average_price</th>\n      <th>address</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>Corridor Seven Coffee Roasters</td>\n      <td>4.7</td>\n      <td>600</td>\n      <td>Near Ketkar Hospital, Sitabuldi, Nagpur</td>\n    </tr>\n    <tr>\n      <th>6</th>\n      <td>BARBECUE</td>\n      <td>4.5</td>\n      <td>650</td>\n      <td>Plot 2B, Mount Road Extension, Near Sadar, Nagpur</td>\n    </tr>\n    <tr>\n      <th>7</th>\n      <td>Uttar Dakshin By Naivedhyam</td>\n      <td>4.5</td>\n      <td>400</td>\n      <td>Mount Road Extension, Near Sadar, Nagpur</td>\n    </tr>\n    <tr>\n      <th>15</th>\n      <td>Domino's Pizza</td>\n      <td>4.4</td>\n      <td>400</td>\n      <td>Plot 7, 8, Ground Floor, Deotare Plaza, Manewada Road, Welekar Nagar, Near Ayodhya Nagar, Nagpur</td>\n    </tr>\n    <tr>\n      <th>18</th>\n      <td>Plan B</td>\n      <td>4.4</td>\n      <td>600</td>\n      <td>301/302, South Ambazari Road, Mate Square, Near Vishal Petrol Pump, Pratap Nagar, Nagpur</td>\n    </tr>\n    <tr>\n      <th>19</th>\n      <td>Checker's</td>\n      <td>4.4</td>\n      <td>600</td>\n      <td>23-25, VCA Complex, Near Civil Lines, Nagpur</td>\n    </tr>\n  </tbody>\n</table>"}
    - utter_ask_email
* deny
    - utter_goodbye

## interactive_story_1
* restaurant_search
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "cuisine"}
* form: inform{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - form: restaurant_form
    - slot{"cuisine": "american"}
    - slot{"requested_slot": "location"}
* explain_slot
    - utter_explain_slot
* affirm
    - utter_ask_location
    - action_listen
* form: inform{"location": "Jabalpur"}
    - slot{"location": "Jabalpur"}
    - restaurant_form
    - slot{"location": "jabalpur"}
    - slot{"requested_slot": "budget"}
* form: inform{"budget": "700 above"}
    - slot{"budget": "700 above"}
    - form: restaurant_form
    - slot{"budget": "700 above"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"email_body": "<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>name</th>\n      <th>aggregate_rating</th>\n      <th>average_price</th>\n      <th>address</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>13</th>\n      <td>Jharokha Restaurant The Arihant Palace</td>\n      <td>4.3</td>\n      <td>800</td>\n      <td>The Arihant Palace, Russell Crossing, Maharshi Dayanand Saraswati Chowk, Napier Town, Jabalpur</td>\n    </tr>\n    <tr>\n      <th>17</th>\n      <td>Takht Hazara - Vijan Mahal</td>\n      <td>4.3</td>\n      <td>2000</td>\n      <td>Mandla Road, Tilhari, Jabalpur</td>\n    </tr>\n  </tbody>\n</table>"}
    - utter_ask_email
* affirm
    - utter_enter_email
* inform{"email_address": "sherardv@live.com"}
    - slot{"email_address": "sherardv@live.com"}
    - action_send_email
    - utter_sent_email
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_1
* out_of_scope
    - utter_out_of_scope
* restaurant_search
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "cuisine"}
* form: inform{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - form: restaurant_form
    - slot{"cuisine": "italian"}
    - slot{"requested_slot": "location"}
* explain_slot
    - utter_explain_slot
    - action_listen
* form: inform{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - restaurant_form
    - slot{"location": "jaipur"}
    - slot{"requested_slot": "budget"}
* form: inform{"budget": "700 above"}
    - slot{"budget": "700 above"}
    - form: restaurant_form
    - slot{"budget": "700 above"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_search_restaurants
    - slot{"email_body": "<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>name</th>\n      <th>aggregate_rating</th>\n      <th>average_price</th>\n      <th>address</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>Steam - Rambagh Palace</td>\n      <td>4.8</td>\n      <td>2800</td>\n      <td>Rambagh Palace, Bhawani Singh Road, C Scheme, Jaipur</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>Tapri Central</td>\n      <td>4.7</td>\n      <td>800</td>\n      <td>B4 E, 3rd Floor, Surana Jewellers, Opposite Central Park, C Scheme, Jaipur</td>\n    </tr>\n    <tr>\n      <th>8</th>\n      <td>Peshawri - ITC Rajputana Hotel</td>\n      <td>4.7</td>\n      <td>3000</td>\n      <td>ITC Rajputana Hotel, Palace Road, Gopalbari, Jaipur</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>The Night Jar</td>\n      <td>4.6</td>\n      <td>1200</td>\n      <td>3rd Floor, Panch Batti, MI Road, Jaipur</td>\n    </tr>\n    <tr>\n      <th>6</th>\n      <td>Farzi Cafe</td>\n      <td>4.6</td>\n      <td>2000</td>\n      <td>Radisson Jaipur City Center, Khasa Kothi Circle, MI Road, Jaipur</td>\n    </tr>\n    <tr>\n      <th>12</th>\n      <td>Jaipur Adda</td>\n      <td>4.5</td>\n      <td>1600</td>\n      <td>Nirwana Hometel, 4 D Villa, Khasa Kothi Circle, Station Road, Bani Park, Jaipur</td>\n    </tr>\n    <tr>\n      <th>13</th>\n      <td>Chokhi Dhani</td>\n      <td>4.5</td>\n      <td>1800</td>\n      <td>Chokhi Dhani Village Resort, 12 Mile, Sitapur, Jaipur</td>\n    </tr>\n    <tr>\n      <th>14</th>\n      <td>OTB - On The Bar B-Q</td>\n      <td>4.5</td>\n      <td>1200</td>\n      <td>6th Floor, Crystal Court Mall, Malviya Nagar, Jaipur</td>\n    </tr>\n    <tr>\n      <th>17</th>\n      <td>The Royal Root - Crowne Plaza Jaipur</td>\n      <td>4.5</td>\n      <td>2000</td>\n      <td>SP 1, Sitapura, RIICO, Sitapur, Jaipur</td>\n    </tr>\n    <tr>\n      <th>18</th>\n      <td>Barbeque Nation</td>\n      <td>4.5</td>\n      <td>1400</td>\n      <td>Shop 1 &amp; 2, 2nd Floor, Jaipur Center Compelx, Sector B, Ashram Marg, Durgapur Bye Pass, PWD Chowk, Durgapura, Jaipur</td>\n    </tr>\n  </tbody>\n</table>"}
    - utter_ask_email
* affirm
    - utter_enter_email
* inform{"email_address": "sherardv@live.com"}
    - slot{"email_address": "sherardv@live.com"}
    - action_send_email
    - utter_sent_email
* goodbye
    - utter_goodbye
