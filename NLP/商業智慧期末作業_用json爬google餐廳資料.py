#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install pandas


# In[4]:


from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import json
import requests
from sklearn.model_selection import train_test_split
import re
import time
from pandas.core.frame import DataFrame
import pandas as pd
import numpy as np
from IPython.display import clear_output


# In[4]:


def remove_symbol(review):
    if '(由 Google 提供翻譯)' in review:
        review=''
    pattern = re.compile(r'[\u4e00-\u9fa5]')
    line = pattern.findall(review.encode().decode())
    t=''
    ## 處理非中文字所形成的沒字串
    for i in line:
        if len(i) > 0:
            t += i
    return t


# In[110]:


## 下載資料
options = webdriver.ChromeOptions()
prefs = {"download.default_directory": r"D:\Jupyter\鼎泰豐_高雄店",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True}
options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(chrome_options=options)
for i in range(1,345):
    print(i)
    a = str(i)
    #https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&pb=!1m2!1y3765758614574346861!2y10663098530229991004!2m2!1i30!2i10!3e1!4m5!3b1!4b1!5b1!6b1!7b1!5m2!1s5B67YLSNM4e2mAWChJKQBg!7e81
    page_source = 'https://www.google.com.tw/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&pb=!1m2!1y3777962672330115261!2y11923744254839123432!2m2!1i'+a+'0!2i10!3e1!4m5!3b1!4b1!5b1!6b1!7b1!5m2!1s7kK7YJfLOrSYr7wP8vaLmAs!7e81'
    driver.get(page_source)


# In[14]:


## 
import os
storename=['高雄店','台中店','新竹店','板橋店','新生店','遠百信義A13店','新光A4店','南西店','101店','天母店','復興店','信義區']
yourPath = 'D:/Jupyter/鼎泰豐_'
#resPath='./reviews/鼎泰豐_'
for name in storename:
    res_reviews=[]
    res_scores=[]
    t=''
    path = yourPath+name
    allFileList = os.listdir(path) ## 所有file的list
    for file in allFileList:
        t=''
        text = open(path+'/'+file, 'r',encoding="utf8")
        for line in text:
            t += line
        pretext = ")]}'"
        res = t.replace(pretext,'')
        soup = json.loads(res)
        ## 
        conlist = soup[2] #名字、評論、時間、評分、圖片
        for i in conlist:
            review = remove_symbol(str(i[3])) #選擇評論
            score = str(i[4]) #選擇分數
            if review != '': # 只取有評論的
                res_reviews.append(review)
                res_scores.append(score)
        text.close()
    res = {"review":res_reviews, "scores":res_scores}
    data=DataFrame(res)#将字典转换成为数据框
    resPath='./reviews/鼎泰豐_%s.csv' % (name)
    print(resPath)
    data.to_csv(resPath,index=0)


# In[113]:


path='./reviews/鼎泰豐_高雄店.csv'
#data.to_csv(path,index=0)


# In[114]:


df = pd.read_csv(path)
df.head()


# In[115]:


len(df)


# In[ ]:




