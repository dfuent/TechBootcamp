# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 17:01:09 2020

Description: Pipeline to explore salary and education breakdown from data 
collected by the Federal Reserve Bank (FRB) during its annual Survey of 
Household Economics and Decisionmaking (SHED). 

Data source: https://www.federalreserve.gov/consumerscommunities/shed_data.htm_
Variable dictionary here: 
https://www.federalreserve.gov/consumerscommunities/files/SHED-2019-codebook.pdf
@author: David Fuentes (dmf4ns@virginia)
"""

import pandas as pd
import datetime as dt # will use to see how long it takes to run my pipeline

start_time = dt.datetime.now() 

a = 'ppfs0596' # FRB variable for salary bands
b = 'ED0'      # FRB variable for education level


# I think there's an issue with some apostrophes in some of the data, so added 
# encoding param:
df = pd.read_csv('public2019.csv', encoding = 'unicode_escape') 

df['Year'] = 2019

sort = {'Under $50,000': 1, '$50,000 - $99,999': 2, '$100,000 - $249,999': 3, 
        '$250,000 - $499,999': 4, '$500,000 - $999,999': 5, 
        '$1,000,000 or more': 6, 'Not sure': 7, 'Refused': 8}

# mapping the sort dict so I can sort & have numeric values for salary bands:
df['sort_key'] = df[a].map(sort) 
df_sort = df.sort_values('sort_key')

# get the inverse of the sort dict:
flip_dict = {value:key for key, value in sort.items()}

# filter the DF for the data I want to graph:
df_fin = df_sort[[a, b, 'sort_key']]

df_fin.rename(columns = {a: 'Salary (USD)', b: 'Education'}, inplace = True)

cross_tab = pd.crosstab(df_fin['sort_key'], df_fin['Education'])

cross_tab.sort_values('sort_key', inplace = True)

cross_tab['Salary (USD)'] = cross_tab.index.to_series().map(flip_dict)

cross_tab.set_index('Salary (USD)', drop = True, inplace = True)

cross_tab.to_excel('ct.xlsx')

cross_tab.plot.barh(title = 'Count of Responses by Salary & Education', grid = True)

cross_tab.plot.barh(subplots = True, title = 'Count of Responses by Salary (USD) & Education', sharey = True, legend = False, grid = True)


# I also want to normalize responses to visualize based on relative % of responses, not count:
l = cross_tab.columns.tolist()

for i in l:
    cross_tab[i] = cross_tab[i] / cross_tab[i].sum()
    
ct_norm = cross_tab.T

ct_norm.to_excel('ct_norm.xlsx') # exported normalized table to Excel to ensure calculation worked

ct_norm.plot.barh(title = 'Normalized Responses by Salary (USD) & Education', grid = True)

ct_norm.plot.barh(stacked = True, title = 'Normalized Responses by Salary (USD) & Education', grid = True)

end_time = dt.datetime.now()

time_diff = (end_time - start_time)
 
print('Graphs have been produced. This script took '+ '%s.%s' % (time_diff.seconds, time_diff.microseconds) + ' seconds to run')