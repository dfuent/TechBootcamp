# Created on Mon Aug 10 11:20:24 2020
# @author: Dave Fuentes (dmf4ns@virginia.edu)
# Bootcamp Exercise 5.7: Creates a function that determines if an input is an English word

install.packages('qdapDictionaries') 

# Learned about package via Google search. See documentation:
# https://cran.r-project.org/web/packages/qdapDictionaries/qdapDictionaries.pdf
# https://www.rdocumentation.org/packages/qdapDictionaries/versions/1.0.7/topics/GradyAugmented

word_check <- function() {
  
  library('qdapDictionaries')
  
  check <- FALSE
  
  while (check == FALSE) {
  word_inp <- tolower(readline(prompt = 'Please enter an English word: '))
  check <- word_inp %in% GradyAugmented
  
  if (check) {
    break
  }
  else {
    print('I\'m sorry. That isn\'t a word.')
    
  }
  }
  print(paste('Thanks! Your word is:', word_inp, sep = ' '))
  
}

word_check()