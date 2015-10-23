# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 19:18:57 2015

@author: m
"""

from scipy import stats
from scipy.stats import chisquare 
import collections
import pandas as pd
import matplotlib.pyplot as plt

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData.dropna(inplace=True)

freq = collections.Counter(loansData['Open.CREDIT.Lines'])

plt.figure()
plt.bar(freq.keys(), freq.values(), width=1)
plt.show()

chi, p = stats.chisquare(freq.values())

import scipy, scipy.stats.chisquare 
observed_values=scipy.array([18,21,16,7,15])
expected_values=scipy.array([22,19,44,8,16])
 
chisquare(observed_values, f_exp=expected_values)

