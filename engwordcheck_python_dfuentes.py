# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 18:29:35 2020

@author: Dave Fuentes (4dmfns@virginia.edu)

Function to determine if an input is an English word
"""

# I am using the words in the Natural Language Toolkit via NLTK corpus.
# For more info, see website: https://www.nltk.org/

import nltk
nltk.download('words')
from nltk.corpus import words

def word_check():    
    
    check = False
    
    while check == False:
        s = input('Please enter an English word: ').strip().lower() 
        check = s in words.words()
        
        if check == False:
         
            print('Sorry. That isn\'t a recognized word.')
        
    else:     
        
        print('Thanks! Your word is ' + s + '.')
        
word_check()