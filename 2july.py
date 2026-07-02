# pagination :
"""
Pagination: The page number in the URL changes.
Looping: for loop visits each page.
Rate Limiting: time.sleep(2) waits 2 seconds before the next request.

"""
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
url = "https://quotes.toscrape.com"

for i in range(1,3):
    url = f"https://quotes.toscrape.com/page/{i}/" 
    reponse = requests.get(url)
    soup = BeautifulSoup(reponse.text, "html.parser")
    print(f"page {i} ")
    author_tag = soup.select("small.author")
    
    for  x in author_tag:
        print(x.text)
    
    time.sleep(0.5)