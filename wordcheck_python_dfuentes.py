# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 18:29:35 2020

@author: Dave Fuentes (4dmfns@virginia.edu)

Function to determine if an input is a string of letters 
(not necessarily an English word)
"""

def string_check():
    
    check = False
    
    while check == False:
        s = input('Please enter a string: ').strip()
        
        if s.isalpha() == False:
            print('Sorry. That isn\'t a string.')
            
        else:
            check = True       
            print('Thanks! Your string is ' + s + '.')
        
string_check()