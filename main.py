import pandas as pd
#import numpy as np
#import smtplib
#import bs4
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
#import requests

title = []
perusahaan = []
#link = []
#year = []
#location = []
#updatedate = []
#lokasi =[]
#gaji = []

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
    
    #for card in all_cards:
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
            
    #for location in soup.find_all('div',{'class': 'JobCardsc__JobcardContainer-sc-hmqj50-0 kWccWU CompactOpportunityCardsc__CompactJobCardWrapper-sc-dkg8my-0 kwAlsu compact_job_card'}):
        #locationtag = location.find('span',{'class': 'CompactOpportunityCardsc__OpportunityInfo-sc-dkg8my-13 fjxsHI'})
        #CompactOpportunityCardsc__HierarchicalLocationSpan-sc-dkg8my-26 gWoWBv
        #if locationtag is not None:
            #location.append(locationtag.text.strip())
        #else:
            #location.append('')
            
    
    #for year in soup.find_all('div',{'class': 'JobCardsc__JobcardContainer-sc-hmqj50-0 kWccWU CompactOpportunityCardsc__CompactJobCardWrapper-sc-dkg8my-0 kwAlsu compact_job_card'}):
        #yeartag = year.find('div',{'class': 'CompactOpportunityCardsc__OpportunityInfo-sc-dkg8my-13 fjxsHI'})
        #if yeartag is not None:
            #year.append(yeartag.text.strip())
        #else:
            #year.append('')
    
    #for updatedate in soup.find_all('div',{'class': 'JobCardsc__JobcardContainer-sc-hmqj50-0 kWccWU CompactOpportunityCardsc__CompactJobCardWrapper-sc-dkg8my-0 kwAlsu compact_job_card'}):
        #updatetag = updatedate.find('div',{'class': 'CompactOpportunityCardsc__UpdatedAtMessage-sc-dkg8my-16 fcqxei'})
        #if updatetag is not None:
            #updatedate.append(updatetag.text.strip())
        #else:
            #updatedate.append('')
    
    #posts = soup.select('div[class="JobCardsc__JobCardWrapper-sc-hmqj50-1 eaQLAc"]>a')
    #for post in posts:
        #link.append('https://glints.com' + post['href'])
    
    
    
    #for linktag in name:
            #link.append(linktag.get('href'))
        
    #for loker in soup.find_all('div',{'class': 'JobCardsc__JobcardContainer-sc-hmqj50-0 kWccWU CompactOpportunityCardsc__CompactJobCardWrapper-sc-dkg8my-0 kwAlsu compact_job_card'}):
        #linkloker = loker.find('a',{'class': 'CompactOpportunityCardsc__CardAnchorWrapper-sc-dkg8my-17 cLLjmr job-search-results_job-card_link'})
        #linklokera = linkloker.find('a', href=True)
        #if linkloker is not None:
            #link.append(linkloker)
        #else:
            #link.append('')
    
    #for loker in soup.find_all('a',{'class': 'CompactOpportunityCardsc__CardAnchorWrapper-sc-dkg8my-17 cLLjmr job-search-results_job-card_link'}):
        #linkloker = loker.find('a',{'class': 'CompactOpportunityCardsc__CardAnchorWrapper-sc-dkg8my-17 cLLjmr job-search-results_job-card_link'})
        #linkloker = loker.find('a', href=True)
        #if linkloker is not None:
            #link.append(linkloker)
        #else:
            #link.append('')
            
        #linkloker = loker.find('a', href=True)
        #if linkloker is not None:
            #link.append(linkloker["href"])
        #else:
            #link.append('')
    
    #for loker in soup.find_all('div',{'class': 'JobCardsc__JobcardContainer-sc-hmqj50-0 kWccWU CompactOpportunityCardsc__CompactJobCardWrapper-sc-dkg8my-0 kwAlsu compact_job_card'}):
        #linkloker = loker.find('div',{'class': 'CompactOpportunityCardsc__Ellipsis-sc-dkg8my-11 jUUwJq'})
        #linkloker = loker.find('a', href=True)
        #if linkloker is not None:
            #link.append(linkloker["href"])
        #else:
            #link.append('')
    
      
    
    print('Scraping status for "{}" : Done' .format(job))
    print()

job()

# Dataframe creation
df = pd.DataFrame({
'Nama_Loker': title,
'Perusahaan': perusahaan
#'lokasi': lokasi 
#'gaji': gaji
})
df

df.to_csv('LokerData.csv')

# push data list to MongoDB
# Establish a client connection to MongoDB
MONGODB_CONNECTION_STRING = os.environ["MONGODB_CONNECTION_STRING"]
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





####################################################################


# #import some packages
# import pandas as pd
# #import numpy as np
# #import smtplib
# import bs4
# from bs4 import BeautifulSoup
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi
# import os
# #import requests

# # scrape process
# #try:
# #   SOME_SECRET = os.environ["SOME_SECRET"]
# #except KeyError:
# #    SOME_SECRET = "Token not available!"
# #     or raise an error if it's not available so that the workflow fails

# title = []
# perusahaan = []
# urllink = []
# #lokasi =[]
# #gaji = []

# def job ():
    
#     #driver = webdriver.Chrome(ChromeDriverManager().install())
#     driver = webdriver.Chrome("chromedriver")
    
#     baseurl= 'https://glints.com'
#     url = 'https://glints.com/id/lowongan-kerja'
#     #url = 'https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276'
    
#     driver.get(url)
    
#     sleep(10)
#     print('Collecting data for "{}"...' .format(job))
   
#     # Locating job container
#     # all_cards = driver.find_elements_by_xpath("//div[@class='CompactJobCardListsc__JobCardListContainer-sc-hzuvo1-0 cRVnOn']")
#     #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class="CompactJobCardListsc__JobCardListContainer-sc-hzuvo1-0 cRVnOn stylessc__CompactJobCardList-sc-gkietk-0 dIUzZN"]')))
#     #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'app')))
#     WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.ID, 'app'))) 
#     sleep(5)
    
#     soup = BeautifulSoup(driver.page_source, "html.parser")
  
#     print('Proses Mining Data')
    
#     #for card in all_cards:

#     for name in soup.find_all('div',{'class': 'CompactOpportunityCardsc__CompactJobCardInfo-sc-dkg8my-6 brXNLA job-card-info'}):
#         nametag = name.find('h3',{'class': 'CompactOpportunityCardsc__JobTitle-sc-dkg8my-7 jJvzUD'})
#         if nametag is not None:
#             title.append(nametag.text.strip())
#         else:
#             title.append('')
                
#     for company in soup.find_all('div',{'class': 'CompactOpportunityCardsc__Ellipsis-sc-dkg8my-11 jUUwJq'}):
#         companytag = company.find('a',{'class': 'CompactOpportunityCardsc__CompanyLink-sc-dkg8my-8 btWyBR'})
#         if companytag is not None:
#             perusahaan.append(companytag.text.strip())
#         else:
#             perusahaan.append('')
    
# #    for url1 in company:
# #        urllinkk = company.find("a",{"class": 'CompactOpportunityCardsc__CompanyLink-sc-dkg8my-8 btWyBR'}.get('href'))
# #        if urllinkk is not None:
# #            urllink.append(baseurl+urllinkk)
# #        else:
# #            urllink.append('')

    
# #   for link in soup.find_all('div',{'class': 'CJobCardsc__JobcardContainer-sc-hmqj50-0 kWccWU CompactOpportunityCardsc__CompactJobCardWrapper-sc-dkg8my-0 kwAlsu compact_job_card'}):
# #       linktag = link.find('a',{'class': 'CompactOpportunityCardsc__CardAnchorWrapper-sc-dkg8my-17 cLLjmr job-search-results_job-card_link'})
# #       linktag_d=urltag.find(href=True)
# #       if linktag_d is not None:
# #           url.append(linktag_d.text.strip())
# #       else:
# #           url.append('')
            
# #     for location in soup.find_all('div',{'class': 'CompactOpportunityCardsc__OpportunityInfo-sc-dkg8my-13 fjxsHI'}):
# #         locationtag = location.find('div',{'class': 'CompactOpportunityCardsc__HierarchicalLocationSpan-sc-dkg8my-26 gWoWBv'})[0].text
# #         if locationtag is not None:
# #             lokasi.append(locationtag.text.strip())
# #         else:
# #             lokasi.append('')
            
#          # ('[class="CompactOpportunityCardsc__HierarchicalLocationSpan-sc-dkg8my-26 gWoWBv"]')[0].text   
#         # ('div[class="TopFoldsc__JobOverViewCompanyLocation-sc-kklg8i-6 gLATOW"]>span>a')[0].text
            
# #     for salary in soup.find_all('div',{'class': 'CompactOpportunityCardsc__OpportunityInfo-sc-dkg8my-13 fjxsHI'}):
# #         salarytag = salary.find('span').text
# #         if salarytag is not None:
# #             gaji.append(salarytag.text.strip())
# #         else:
# #             gaji.append('')

# #     for salary in soup.find_all('div',{'class': 'CompactOpportunityCardsc__OpportunityInfo-sc-dkg8my-13 fjxsHI'}):
# #         salarytag = salary.find_element("//span[contains(@class,'CompactOpportunityCardsc__OpportunityInfo-sc-dkg8my-13 fjxsHI')]").text
# #         if salarytag is not None:
# #             gaji.append(salarytag.text.strip())
# #         else:
# #             gaji.append('')
        
# #       driver.find_element_by_xpath("//span[contains(@class,'Trsdu')]").text
# #       find_element(By.XPATH,"//span[@dir='auto']/span").get_attribute("innerText")       
#     print('Crawling status for "{}" : Done' .format(job))
#     print()


# job()


#  # Dataframe creation
# df = pd.DataFrame({
# 'title': title,
# 'perusahaan': perusahaan
# #'lokasi': lokasi 
# #'gaji': gaji
# })
# df

# df.to_csv('LokerData.csv')

# # push data list to MongoDB
# # Establish a client connection to MongoDB
# MONGODB_CONNECTION_STRING = os.environ["MONGODB_CONNECTION_STRING"]
# client = MongoClient(MONGODB_CONNECTION_STRING)

# # convert to dictionary for uploading to MongoDB
# df = df.to_dict('records')

# # point to lokerDB collection 
# db = client.lokerDB

# # emtpy symbols collection before inserting new documents
# db.datalok.drop()

# # insert new documents to collection
# db.datalok.insert_many(df)

