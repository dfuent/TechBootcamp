# Date: 8/10/2020
# Author: Dave Fuentes (dmf4ns@virginia.edu)
# Simple function which prints how long it took to run itself. Add code and/or function(s)
# within the body if you would like to see how long it takes for them to run


stop_watch <- function() {

  start_time <- Sys.time()
  
  # enter code in here
  # I'm putting in a loop to kill some time so output isn't 0
  
  x <- 0
  
  for (i in 1:10000000) {
    
    x <- x + i
  }
  
  end_time <- Sys.time()
  elapsed_time <- round(end_time - start_time, digits = 4)
  
  print(paste('The script ran in', elapsed_time, 'seconds', sep = ' '))
}

stop_watch() # run the function