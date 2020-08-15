# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 17:01:09 2020

Description: Pipeline to explore savings & investments and education breakdown from data 
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

a = 'ppfs0596' # FRB variable for approx savings and investments
b = 'ED0'      # FRB variable for education level


# I think there's an issue with some apostrophes in some of the data, so added 
# encoding param:
df = pd.read_csv('public2019.csv', encoding = 'unicode_escape') 

df['Year'] = 2019

# set up sorting dictionaries and do some data cleansing:
sort = {'Under $50,000': 1, '$50,000 - $99,999': 2, '$100,000 - $249,999': 3, 
        '$250,000 - $499,999': 4, '$500,000 - $999,999': 5, 
        '$1,000,000 or more': 6, 'Not sure': 7, 'Refused': 8}

# need to clean up the edu data a bit to fix apostrophe character:
edu_clean = {'Less than High School degree':'L.T. High School degree', 
           'High school degree or GED':'High school or GED', 
           'Some college but no degree (including currently enrolled in college)':'Some college but no degree (incl. college students)', 
           'Certificate or technical degree':'Certificate or technical degree',
           'Associate degree':'Associate degree',
           'Bachelor\x92s degree': 'Bachelor’s degree', 
           'Master\x92s degree': 'Master’s degree', 'Doctoral Degree':'Doctoral Degree', 'Professional degree (e.g. MBA, MD, JD)':'Professional degree (e.g. MBA, MD, JD)'} 

sort_edu = {'L.T. High School degree':1, 'High school or GED':2, 
           'Some college but no degree (incl. college students)':3, 
           'Certificate or technical degree':4, 'Associate degree':5, 
           'Bachelor’s degree':6, 'Master’s degree':7, 'Doctoral Degree':8, 
           'Professional degree (e.g. MBA, MD, JD)':9} 

df[b] = df[b].map(edu_clean)

# mapping the sort dict so I can sort & have numeric values for sorting:
df['sort_key'] = df[a].map(sort) 
df['sort_key2'] =df[b].map(sort_edu)

df_sort = df.sort_values('sort_key')

# get the inverse of the sort dict:
flip_dict = {value:key for key, value in sort.items()}
flip_dict2 = {value:key for key, value in sort_edu.items()}

# filter the DF for the data I want to graph:
df_fin = df_sort[[a, b, 'sort_key', 'sort_key2']]

df_fin.rename(columns = {a: 'Savings & Investments (USD)', b: 'Education'}, inplace = True)

# crosstab will help set up the counts and, later, the percentages
cross_tab = pd.crosstab(df_fin['sort_key'], df_fin['sort_key2'])

cross_tab.sort_values('sort_key', inplace = True)

# want to name the columns back to meaningful values rather than numbers
l = []

for i in cross_tab.columns:
    
    l.append(flip_dict2.get(i))

cross_tab.columns = l
    
cross_tab['Savings & Investments (USD)'] = cross_tab.index.to_series().map(flip_dict)

cross_tab.set_index('Savings & Investments (USD)', drop = True, inplace = True)

cross_tab.to_excel('ct.xlsx')

cross_tab.plot.barh(title = 'Count of Responses by Tot. Savings/Investments & Education', grid = True)

cross_tab.plot.barh(subplots = True, title = 'Count of Responses by Tot. Savings/Investments & Education', sharey = True, legend = False, grid = True)


# I also want to normalize responses to visualize based on relative % of responses, not count:
l = cross_tab.columns.tolist() 

for i in l:
    cross_tab[i] = cross_tab[i] / cross_tab[i].sum()
    
ct_norm = cross_tab.T

ct_norm.to_excel('ct_norm.xlsx') # exported normalized table to Excel to ensure calculation worked

ct_norm.plot.barh(title = 'Normalized Responses by Tot. Savings/Investments & Education', grid = True)

ct_norm.plot.barh(stacked = True, title = 'Normalized Responses byTot. Savings/Investments & Education', grid = True)

end_time = dt.datetime.now()

time_diff = (end_time - start_time)
 
print('Graphs have been produced. This script took '+ '%s.%s' % (time_diff.seconds, time_diff.microseconds) + ' seconds to run')
