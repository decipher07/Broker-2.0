#!/usr/bin/env python
# coding: utf-8

# In[44]:


from selenium import webdriver
import time
import pandas as pd

op = webdriver.ChromeOptions()
op.add_argument('headless')
browser = webdriver.Chrome(executable_path='./chromedriver', options = op)


# In[45]:


initial_data = pd.read_excel('Stock-URL.xlsx')
initial_data


# In[46]:


def rsi_value_of_given_stock ( stock_name, stock_url ):
    
    daily_rsi_url = stock_url + 'daily'
    weekly_rsi_url = stock_url + 'weekly'
    monthly_rsi_url = stock_url + 'monthly'
    
    browser.get(daily_rsi_url)
    daily_rsi_value = browser.find_element_by_xpath('//*[@id="techindd"]/div[3]/table/tbody[2]/tr[1]/td[2]/strong').text
    
    browser.get(weekly_rsi_url)
    weekly_rsi_value = browser.find_element_by_xpath('//*[@id="techind"]/div[3]/table/tbody[2]/tr[1]/td[2]/strong').text
    
    browser.get(monthly_rsi_url)
    monthly_rsi_value = browser.find_element_by_xpath('//*[@id="techind_m"]/div[3]/table/tbody[2]/tr[1]/td[2]/strong').text
    
    # Date
    date_for_the_given_stock = browser.find_element_by_xpath('//*[@id="div_bse_livebox_wrap"]/div[1]/div[1]/div/div[1]/span').text

    # Closing
    closing_value = browser.find_element_by_xpath('//*[@id="div_nse_livebox_wrap"]/div[1]/div[1]/div/div[2]/span[1]').text
    
    return [daily_rsi_value, weekly_rsi_value, monthly_rsi_value, date_for_the_given_stock, closing_value]


# In[66]:


# Adding Storing Index Values 
data_record = pd.read_excel('Record-Data.xlsx', header=0, index_col=0)
data_record


# In[67]:


for index, row in initial_data.iterrows():
    data_for_stock = rsi_value_of_given_stock (row["Name of Stock"], row["Url"])
    data_record.loc[row["Name of Stock"], "Daily as on {}".format(data_for_stock[3])] = data_for_stock[0]
    data_record.loc[row["Name of Stock"], "Weekly as on {}".format(data_for_stock[3])] = data_for_stock[1]
    data_record.loc[row["Name of Stock"], "Monthly as on {}".format(data_for_stock[3])] = data_for_stock[2]
    data_record.loc[row["Name of Stock"], "Closing as on {}".format(data_for_stock[3])] = data_for_stock[4]

data_record


# In[69]:


data_record.to_excel('Record-Data.xlsx')


# In[39]:


# # for index, row in initial_data.iterrows():
#     print (rsi_value_of_given_stock (row["Name of Stock"], row["Url"]) )
# for index, row in initial_data.iterrows():
#     print (row["Name of Stock"], row["Url"])


# In[71]:


# Adding Storing Index Values 
# data_record = pd.read_excel('Record-Data.xlsx', header=0, index_col=0)
# data_record


# In[70]:


# data_record.loc["SOmething", "Data as on asome data "] = 4
# data_record


# In[ ]:




