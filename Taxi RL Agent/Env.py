# Import routines

import numpy as np
import math
import random

# Defining hyperparameters
m = 5 # number of cities, ranges from 1 ..... m
t = 24 # number of hours, ranges from 0 .... t-1
d = 7  # number of days, ranges from 0 ... d-1
C = 5 # Per hour fuel and other costs
R = 9 # per hour revenue from a passenger


class CabDriver():

    def __init__(self):
        """initialise your state and define your action space and state space"""
        self.action_space = [[i,j] for i in range(5) for j in range(5) if ((i!=j) or ((i==0) and (j==0)))]
        self.state_space = [[i,j,k] for i in range(5) for j in range(24) for k in range(7)]
        self.state_init = random.choice(self.state_space)

        # Start the first round
        self.reset()


    ## Encoding state (or state-action) for NN input

    def state_encod_arch1(self, state):
        """convert the state into a vector so that it can be fed to the NN. This method converts a given state into a vector format. Hint: The vector is of size m + t + d."""
        
        state_encode = np.zeros(m+t+d)
        state_ind= state[0]
        time_ind= m + state[1]
        day_ind= m + t + state[2]
        
        state_encode[state_ind] = 1
        state_encode[time_ind] = 1
        state_encode[day_ind] = 1
        
        return state_encode


    # Use this function if you are using architecture-2 
    # def state_encod_arch2(self, state, action):
    #     """convert the (state-action) into a vector so that it can be fed to the NN. This method converts a given state-action pair into a vector format. Hint: The vector is of size m + t + d + m + m."""

        
    #     return state_encod


    ## Getting number of requests

    def requests(self, state):
        """Determining the number of requests basis the location. 
        Use the table specified in the MDP and complete for rest of the locations"""
        # loc- Location, req- Requests
        loc = state[0]
        if loc == 0:
            req = np.random.poisson(2)
        elif loc == 1:
            req = np.random.poisson(12)
        elif loc == 2:
            req = np.random.poisson(4)
        elif loc == 3:
            req = np.random.poisson(7)
        elif loc == 4:
            req = np.random.poisson(8)

            
        if req >15:
            req =15

        possible_actions_index = random.sample(range(1, (m-1)*m ), req) # (0,0) is not considered as customer request
        actions = [self.action_space[i] for i in possible_actions_index]

        
        actions.append([0,0])

        return possible_actions_index,actions   



    
    
    
    #new_time_day = New time of the day
    #new_day_week = New day of the week
    def new_time(self,time,day,time_taken):
        new_time_day = time + math.ceil(time_taken)
        new_day_week = day
        if new_time_day > 23:
            new_time_day = new_time_day % 24
            new_day_week += 1
            if new_day_week > 6:
                new_day_week = new_day_week % 7
        return new_time_day,new_day_week
    
    
    
    #time_day = Time of the day
    #day_week = Day of the week
    def reward_func(self, state, action, Time_matrix):
        """Takes in state, action and Time-matrix and returns the reward"""
        reward = 0
        cab_pos = state[0]
        pickup_pos = action[0]
        drop_pos = action[1]
        time_day = state[1]
        day_week = state[2]
        new_time_day = time_day
        new_day_week = day_week
        
        
        if cab_pos!=pickup_pos: 
            time_taken = Time_matrix[cab_pos][pickup_pos][time_day][day_week]
            new_time_day,new_day_week = self.new_time(time_day,day_week,time_taken)
        
        if (pickup_pos == 0) and (drop_pos==0):
            reward = -C
            
        else:
            
            reward = R*Time_matrix[pickup_pos][drop_pos][new_time_day][new_day_week] - C*(Time_matrix[pickup_pos][drop_pos][new_time_day][new_day_week] + Time_matrix[cab_pos][pickup_pos][time_day][day_week])
        
        
        return reward




    def next_state_func(self, state, action, Time_matrix):
        """Takes state and action as input and returns next state"""
        next_state = []
        cab_pos = state[0]
        pickup_pos = action[0]
        drop_pos = action[1]
        time_day = state[1]
        day_week = state[2]
        
        new_time_day = time_day
        new_day_week = day_week
        
        total_time = 0
        
        if cab_pos!=pickup_pos: 
            time_taken = Time_matrix[cab_pos][pickup_pos][time_day][day_week]
            new_time_day,new_day_week = self.new_time(time_day,day_week,time_taken)
            total_time += time_taken
        
        if (pickup_pos == 0) and (drop_pos==0):
            total_time += 1
            new_time_day,new_day_week = self.new_time(time_day,day_week,1)
            next_state = [cab_pos,new_time_day,new_day_week]
        
        else:
            time_taken = Time_matrix[pickup_pos][drop_pos][new_time_day][new_day_week]
            total_time += time_taken
            final_time_day,final_day_week = self.new_time(new_time_day,new_day_week,time_taken)
            next_state = [drop_pos,final_time_day,final_day_week]
        
        return next_state,total_time




    def reset(self):
        return self.action_space, self.state_space, self.state_init
