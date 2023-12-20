#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import pandas as pd
from bs4 import BeautifulSoup


# In[ ]:


import re

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


# In[ ]:


names = pd.read_excel('명단.xlsx',header = None, names = ['닉네임'])


# In[ ]:


url_head = 'https://maple.gg/u/'


# In[ ]:


chart = pd.DataFrame(columns = ['닉네임','레벨','직업','길드','무릉','업적','유니온'])


# In[ ]:


iterations = 1
for nickname in names['닉네임']:
    
    print(iterations/len(names['닉네임'])*100, '% Complete')
    iterations+=1
    
    url = url_head+nickname

    resp = requests.get(url)
    soup = BeautifulSoup(resp.text,"html.parser")
    #정보
    level = cleanhtml(str(soup.find("span",{"class":"level"})))
    job = cleanhtml(str(soup.find("span",{"class":"job"})))
    guild = cleanhtml(str(soup.find("div",{"class":"guild"})))

    box = soup.find("section",{"class":"sc-e8a6934a-0 iHQint"})
    mulung = cleanhtml(str(box.find("div",{"class":"sc-32380e67-2 cMvdPK"})))
    achievements = cleanhtml(str(box.find("div",{"class":"sc-32380e67-2 ebQuqd"})))
    union = cleanhtml(str(box.find("div",{"class":"sc-32380e67-2 gyckEt"})))
    
    appender = []
    appender = [nickname, level, job, guild, mulung, achievements, union]    
    chart.loc[len(chart)] = appender


# In[ ]:


import datetime
suffix = datetime.datetime.now().strftime('%y%m%d')
chart.to_excel(suffix+"연메동 레벨표.xlsx", index = False)


# In[ ]:


print('저장완료')

