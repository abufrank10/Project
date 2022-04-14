#!/usr/bin/env python
# coding: utf-8

# In[1]:


import import_ipynb


# In[2]:


import numpy as np
import nashpy as ns
from itertools import permutations
import lemkeHowson1 as lemkeHowson
import matrix
import rational
import multiprocessing
import matplotlib.pyplot as plt
import csv


# In[3]:


res={}
with open('paper_result_version1', mode='r') as f:
    reader=csv.reader(f)
    for row in reader:
        row[0]=int(row[0])
        for i in range(1, len(row)):
            row[i]=row[i].replace('(','')
            row[i]=row[i].replace(')','')
            row[i]=row[i].replace(',','')
            row[i]=tuple(map(int, row[i].split(' ')))
        print(row)
        res[row[0]]=[row[i] for i in range(1, 4)]
        
# dict_from_csv={int(k): v for k, v in dict_from_csv.items()}

print(res)


# In[4]:


eposide=[i for i in range(30)]
print(eposide)


# In[8]:


price=[]
fix=[]
eposide=[i for i in res]
for i in range(len(res)):
    avg_price_i=(res[i+5][0][0]+res[i+5][1][0]+res[i+5][2][0])/3
    price.append(avg_price_i)
    avg_fix_i=(res[i+5][0][1]+res[i+5][1][1]+res[i+5][2][1])/3
    fix.append(avg_fix_i)
    print(avg_price_i, avg_fix_i)

plt.figure(figsize=(12,3))
plt.xlim(0, 30) 
plt.ylim(0, 30)
plt.plot(eposide, price, 'r')
plt.plot(eposide, fix, 'b')
plt.legend(labels=['P', 'F'])


# In[ ]:




