# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 15:58:52 2020

@author: fuent
"""

def list_print():
    
    inp = ''
    l = []
    
    while inp != '*DONE*':
    
        inp = input('Please enter an item for your list. Type *DONE* once you\'ve entered all of your elements: ')
        l.append(inp)
        
    l.remove('*DONE*')
    print('Thanks. Your list is: ')
    
    for i in l:
        print(i)
        
        

list_print()        