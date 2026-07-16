"""
Session 9 - Cleaning & Saving Scraped Data Save as: CSV Excel JSON Handle missing values Practical: Clean scraped dataset using pandas.

id    name    age    salary   
101   tisha   20      90000 
102           19      80000
103   vansh           70000 
104   sujal   22      95000
105   mayank  21    

# insights  : 
function  : 
1. missing value : df.isnull()
2. fill missing value : df.fillna()
"""

# read csv file  : 
"""
import pandas as pd

df =pd.read_csv("customer_data.csv")
# print(df)

missing_value = df.isnull().sum()
print(missing_value)
"""
"""
Customer_ID        1
Gender             1
City               1
Age                0
Purchase_Amount    1
Orders             0
"""

"""df['Customer_ID']=df['Customer_ID'].fillna("C020")
df['Gender']=df['Gender'].fillna("UNKNOWN")
df['City']=df['City'].fillna("UNKNOWN")

df['Purchase_Amount']=df['Purchase_Amount'].fillna(df['Purchase_Amount'].mean()).astype(int)
"""
# print(df.info())

"""print(df.head())  # default 5 rows  first 5 rows

df.to_csv("cleaned_data.csv",index=False)
df.to_excel("cleaned_data.xlsx",index=False)

df.to_json("cleaned_data.json",orient="records",indent=4)

"""

import pandas as pd
import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

for i in range(1,11):
    driver = webdriver.Chrome()

    driver.get(f"https://quotes.toscrape.com/js/page/{i}")

    WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME,"tag"))
    )

    # tag_item =driver.find_elements(By.CLASS_NAME,"tag")

    # tag =driver.find_elements(By.CLASS_NAME,'a')

    # print(f"-------page{i} ------------")

    # for i in tag_item:
    #     tag = i.find_elements(By.TAG_NAME,"a").text
    #     print(tag)
    #     # print(tag.get_attribute("href"))

    # for item in tag_item:

    #     links = item.find_elements(By.TAG_NAME,"a")

    #     for link in links:
    #         print(link.text)
    # for item in tag_item:
    #     print(item.get_attribute("outerHTML"))
    # driver.quit()
    tags = driver.find_elements(By.CLASS_NAME, "tag")

    for tag in tags:
        print("Tag :", tag.text)
        print("Link:", tag.get_attribute("href"))
    
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

for page in range(1, 11):

    driver.get(f"https://quotes.toscrape.com/js/page/{page}/")

    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "tag"))
    )

    tags = driver.find_elements(By.CLASS_NAME, "tag")

    print(f"\n-------- Page {page} --------")

    for tag in tags:
        print("Tag :", tag.text)
        print("Link:", tag.get_attribute("href"))
        print("-" * 40)

driver.quit()"""