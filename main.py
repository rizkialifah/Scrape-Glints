import pandas as pd
import numpy as np
import smtplib
import bs4
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


title = []
perusahaan = []

def job ():
    
    driver = webdriver.Chrome("chromedriver")
    
    baseurl = 'https://glints.com'
    url = 'https://glints.com/id/opportunities/jobs/explore?keyword=statistika&country=ID&locationName=Indonesia'
 
    driver.get(url)
    
    sleep(10)
    #scroll_pause_time = 10
    print('Collecting data for "{}"...' .format(job))
   
    # Locating job container
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.ID, 'app'))) 
    last_height = driver.execute_script("return document.body.scrollHeight")
    driver.execute_script("""
        var scroll = document.body.scrollHeight / 10;
        var i = 0;
        function scrollit(i) {
           window.scrollBy({top: scroll, left: 0, behavior: 'smooth'});
           i++;
           if (i < 100) {
            setTimeout(scrollit, 1000, i);
            }
        }
        scrollit(i);
        """) 
    
    #sleep(5)
    #time.sleep(scroll_pause_time)
    new_height = driver.execute_script("return document.body.scrollHeight")
    
    if new_height == last_height:
        driver.execute_script("window.scrollTo(0, window.scrollY + 500);")
        sleep(10)
    
    soup = BeautifulSoup(driver.page_source, "html.parser")
  
    print('Proses Mining Data')
    
    
    #Getting job vacancy name
    for name in soup.find_all('div',{'class': 'JobCardsc__JobcardContainer-sc-hmqj50-0 kWccWU CompactOpportunityCardsc__CompactJobCardWrapper-sc-dkg8my-0 kwAlsu compact_job_card'}):
        nametag = name.find('h3',{'class': 'CompactOpportunityCardsc__JobTitle-sc-dkg8my-7 jJvzUD'})
        if nametag is not None:
            title.append(nametag.text.strip())
        else:
            title.append('')
    
    for company in soup.find_all('div',{'class': 'JobCardsc__JobcardContainer-sc-hmqj50-0 kWccWU CompactOpportunityCardsc__CompactJobCardWrapper-sc-dkg8my-0 kwAlsu compact_job_card'}):
        companytag = company.find('a',{'class': 'CompactOpportunityCardsc__CompanyLink-sc-dkg8my-8 btWyBR'})
        if companytag is not None:
            perusahaan.append(companytag.text.strip())
        else:
            perusahaan.append('')
    
    print('Scraping status for "{}" : Done' .format(job))
    print()

job()

# Dataframe creation
df = pd.DataFrame({
'Nama_Loker': title,
'Perusahaan': perusahaan
})
df

df.to_csv('LokerData.csv')

# push data list to MongoDB
# Establish a client connection to MongoDB
MONGODB_CONNECTION_STRING = os.environ['MONGODB_CONNECTION_STRING']
client = MongoClient(MONGODB_CONNECTION_STRING)

# convert to dictionary for uploading to MongoDB
df = df.to_dict('records')

# point to lokerDB collection 
db = client.lokerDB

# emtpy symbols collection before inserting new documents
db.datalok.drop()

# insert new documents to collection
db.datalok.insert_many(df)

print("Completed")
