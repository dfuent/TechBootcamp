# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 15:47:59 2020

@author: dfuentes (dmf4ns@virginia.edu)

Bootcamp Exercise 5.4: Creates a function which prints the time it took to run itself
"""

def stop_watch():
    
# function displays how long it takes to run

    import datetime as dt

    start_time = dt.datetime.now()
    
    # input more code here if you'd like to
    
    for i in range(10000000):
        
        # kill some time so output isn't 0
        
        i += i
     
    end_time = dt.datetime.now()
    
    time_diff = (end_time - start_time)
     
    print('Your function took '+ '%s.%s' % (time_diff.seconds, time_diff.microseconds) + ' seconds to run')
     
     
stop_watch()