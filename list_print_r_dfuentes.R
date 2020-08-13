# Created on Mon Aug 10 11:20:24 2020
# @author: Dave Fuentes (dmf4ns@virginia.edu)
# Bootcamp Exercise 5.7: Creates a function that takes a list as input from the user, 
# sets it to a variable, and prints each element

list_inp <- function() {
  
  list_item <- ''
  l = list()
  
  while (list_item != 'I AM DONE') {
  
  list_item <- readline(prompt = 'Please input items for the list. Type I AM DONE if finished: ')
  
  if (list_item != 'I AM DONE') {
  l <- c(l, list_item)
  }
  else {
  break }
  }
  
  if (length(l) == 0) {
    print('Empty List!')
  }
  else{
  for (i in l) {
  print(i)
  }
  }
  
}

list_inp()

