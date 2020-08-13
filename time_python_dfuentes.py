# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 15:10:53 2020

@author: Dave Fuentes (dmf4ns@virginia.edu)

Bootcamp Exercise 5.3: Creates a function which prints the current time formatted so it is legible
"""

# define function to output current time according to your comp


def current_time():
    
    import datetime as dt
    
    curr_time = dt.datetime.now()
    form_time= curr_time.strftime('%m/%d/%Y %H:%M:%S') # added as separate line so it's easier to read

    print('The time is now ' + form_time)
     
current_time()
