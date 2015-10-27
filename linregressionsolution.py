# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 15:10:02 2015

@author: m
"""

# linear regression code from the solution that was provided (copied over)

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

loansData=pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

print loansData['Interest.Rate'][0:5]
print loansData['Loan.Length'][0:5]
print loansData['FICO.Range'][0:5]

loansData['Interest.Rate'] = loansData['Interest.Rate'].map(lambda x: x.rstrip('%'))
loansData['Loan.Length'] = loansData['Loan.Length'].map(lambda x: x.rstrip ('months'))

print loansData['Interest.Rate'][0:5]
print loansData['Loan.Length'][0:5]
A = loansData['Fico.Score'].tolist()
FICO = []
loansData.columns
for j in range (len(A)):
    B = A(j).split("-")
    C = float(B[0])
    FICO.append(C)
loansData['FICO.Score']= FICO

plt.figure()
p=loansData['FICO.Score'].hist()
plt.show()

loansData['Interest.Rate'] = loansData['Interest.Rate'].astype(float)
intrate = loansData['Interest.Rate']
intrate = [int(x) for x in intrate]
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']

y = np.matrix(intrate).transpose()  
print (y)
x1 = np.matrix(fico).transpose()    
x2 = np.matrix(loanamt).transpose()
print(x1)
print(x2)

x = np.column_stack([x1,x2])


X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()
f.summary()




