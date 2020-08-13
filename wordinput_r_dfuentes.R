# Created on Mon Aug 10 18:18:24 2020
# @author: Dave Fuentes (dmf4ns@virginia.edu)
# Bootcamp Exercise 5.5: Creates a function that takes a keyboard input from the user, 
# sets it to a variable, and prints it 

word_output <- function() {
  word <- readline(prompt = 'What would you like me to print? Type here: ')
  print(paste('Cool! Here is your word:', word, sep = ' '))
  
}

word_output()
