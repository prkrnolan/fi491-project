# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 18:22:25 2020

@author: parker nolan
"""

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.style.use('ggplot')

loans_old = pd.read_csv('loan.csv', header=0, low_memory = False, nrows=400000)

loans_new = pd.read_csv('lendingclub-individual.csv', header=0, low_memory = False)

lcd = pd.concat([loans_new, loans_old])
#
lcd.groupby(['grade', 'issue_d']).mean()['funded_amnt'].unstack().plot(kind='bar',figsize=(20, 12), title= 'Average loan amount by credit grade and date')

lcd.groupby(['grade', 'issue_d']).count()['funded_amnt'].unstack().plot(kind='bar',figsize=(20, 12), title = 'Count of loans issued by credit grade and date')

lcd.groupby(['grade', 'issue_d']).median()['funded_amnt'].unstack().plot(kind='bar',figsize=(20, 12), title= 'Median loan amount by credit grade and date')

lcd.groupby(['grade', 'purpose']).median()['funded_amnt'].unstack().plot(kind='bar',figsize=(20, 12), title= 'Median loan amount by credit grade and application type')

lcd.groupby(['grade', 'purpose']).count()['funded_amnt'].unstack().plot(kind='bar',figsize=(20, 12), title= 'Count of loans by credit grade and application type')

lcd.groupby(['grade', 'purpose']).mean()['funded_amnt'].unstack().plot(kind='bar',figsize=(20, 12), title= 'Average loan amount by credit grade and application type')

#lcd['int_rate'].plot(figsize=(20, 10), lw=.1)
#ask = lcd['loan_amnt']
#real = lcd['funded_amnt_inv']
#ask.mean().plot()
#((real/ask)*100).mean().plot(figsize=(10, 10), lw=.8)