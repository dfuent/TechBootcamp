
# Created on Wed Aug 12 18:01:09 2020

# Description: Pipeline to explore salary and education breakdown from data 
# collected by the Federal Reserve Bank (FRB) during its annual Survey of 
# Household Economics and Decisionmaking (SHED). 

# Data source: https://www.federalreserve.gov/consumerscommunities/shed_data.htm_
# Variable dictionary here: https://www.federalreserve.gov/consumerscommunities/files/SHED-2019-codebook.pdf
# @author: David Fuentes (dmf4ns@virginia)


library(ggplot2)


a <- 'ppfs0596' # FRB variable for salary bands
b <- 'ED0'      # FRB variable for education level

df_frb <- read.csv('public2019.csv')
df_frb['Year'] <- 2019

names(df_frb)[names(df_frb) == a] <- 'Salary'
names(df_frb)[names(df_frb) == b] <- 'Education_Level'

df_frb$Salary <- factor(df_frb$Salary, levels = c('Under $50,000', '$50,000 - $99,999', '$100,000 - $249,999', 
                              '$250,000 - $499,999', '$500,000 - $999,999', 
                              '$1,000,000 or more', 'Not sure', 'Refused'))

df_frb <- df_frb[order(df_frb$Salary),]

df_frb['Rel%'] <- df_frb['Salary']

g <- ggplot(df_frb, aes(x = Salary, fill = Education_Level)) + geom_bar(position = 'dodge') + theme(axis.text.x = element_text(angle = 90)) + coord_flip()

g + ggtitle("Count of Responses by Salary (USD) & Education") 

g + facet_grid(rows = vars(Education_Level)) + ggtitle("Count of Responses by Salary (USD) & Education")

t <- table(df_frb$Salary, df_frb$Education_Level)

t_prop <- prop.table(t, 2)
t_prop <- as.data.frame.matrix(t_prop)

t_stack <- data.frame(rows = rownames(t_prop), stack(t_prop))
t_stack <- t_stack[order(t_stack$rows),]

#print(t)
#print(t_stack)

ggplot(t_stack, aes(x = rows, y = values, fill = ind)) + geom_bar(position = 'dodge', stat = 'identity') +  facet_grid(rows = vars(ind)) + coord_flip() + ggtitle('Normalized Responses by Salary (USD) & Education') + labs(y = '%', x = 'Salary', color = 'Education level')

ggplot(t_stack, aes(x = ind, y = values, fill = rows)) + geom_bar(position = 'stack', stat = 'identity')  + coord_flip() + ggtitle('Normalized Responses by Salary (USD) & Education') + labs(y = '%', y = 'Education Level', color = 'Salary') #+  facet_grid(rows = vars(ind))+ 
