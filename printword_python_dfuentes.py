# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 18:18:24 2020

@author: Dave Fuentes (dmf4ns@virginia.edu)

Bootcamp Exercise 5.5: Creates a function that takes a keyboard input from the user, 
sets it to a variablE, and prints it 
"""

def input_word():
    
    word = input('What would you like me to print? Type here:' )
    print('Thanks! Here\'s your word: ' + word)
    
input_word()