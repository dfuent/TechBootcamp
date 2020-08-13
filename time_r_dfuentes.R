# Date: 8/10/2020
# Author: Dave Fuentes (dmf4ns@virginia.edu)
# Simple function which prints the current time according to your computer

current_time <- function() {
  curr_time <- Sys.time()
  form_time <- format(curr_time, '%m/%d/%y %H:%M:%S')
  print(paste('The current time is', form_time, sep = ' '))
}

current_time()



