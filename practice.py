import  requests
from bs4 import BeautifulSoup

# ex:1 
'''
html = """
<h1>STUDENTS </h1>
<p>my name is  dishant. i am a student</p>
<title>INTRODUCTION</title>
    
    """
beautiful_soup = BeautifulSoup(html,"html.parser")

h1_tag  = beautiful_soup.find("h1")
p_tag = beautiful_soup.find("p")

print(h1_tag.text)
print(p_tag.text)
'''
#ex:2 

from bs4 import BeautifulSoup

html = """
<html>
<head>
    <title>Student Information</title>
</head>

<body>

    <h1 id="main_heading">Student Details</h1>

    <p class="description">
        This is a web scraping demo.
    </p>

    <div>
        <span>Name: Dishant Shah</span>
    </div>

    <a href="https://www.google.com">Google</a>

    <ul>
        <li>Python</li>
        <li>Pandas</li>
        <li>NumPy</li>
    </ul>

    <table border="1">
        <tr>
            <th>Name</th>
            <th>Age</th>
        </tr>

        <tr>
            <td>Dishant</td>
            <td>25</td>
        </tr>
    </table>

</body>
</html>
"""

"""soup = BeautifulSoup(html, "html.parser")

h1_tag = soup.find("h1").text
p_tag = soup.find("p").text
title_tag = soup.find("title").text
span_tag = soup.find("span").text
link_tag = soup.find("a")['href']

for i in soup.find_all("li"):
    print(i.text)

for j in soup.find_all("td"):
    print(j.text)
print(h1_tag)
print(p_tag)
print(title_tag)
print(span_tag)
print(link_tag)
"""
#ex :1  ===================================================================
"""import requests
from bs4 import BeautifulSoup

# Fetch webpage
url = "https://quotes.toscrape.com"
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Title
print("Title:", soup.title.text)

# First Quote
quote = soup.find("span", class_="text")
print("\nFirst Quote:")
print(quote.text)

# First Author
author = soup.find("small", class_="author")
print("\nAuthor:")
print(author.text)

# All Quotes
print("\nAll Quotes:")
quotes = soup.find_all("span", class_="text")

for q in quotes:
    print(q.text)
    """
    
#ex :2  ===================================================================
"""
import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

title = soup.find("title")
p_tag = soup.find("p")
div_tag = soup.find("div")
link_tag = soup.find("a")["href"]

print("Title:", title.text)
print("Paragraph:", p_tag.text)
print("Div:", div_tag.text[:100])  # first 100 chars
print("Link:", link_tag)
"""
"""
Task 1: Extract All Book Names
books = soup.find_all("h3")
for book in books:
    print(book.a["title"])

Task 2: Extract All Prices 
prices = soup.find_all("p", class_="price_color")
for price in prices:
    print(price.text)
    
Task 3: Extract Book Name + Price 
books = soup.find_all("h3")
prices = soup.find_all("p", class_="price_color")
for book, price in zip(books, prices):
    print(book.a["title"], "-", price.text)

"""

# get : 
import requests

url = "https://jsonplaceholder.typicode.com/posts"

"""
response = requests.get(url)
print("Status Code:", response.status_code)
print(response.json()[0])
"""
# get req with params : its generated URL  : https://jsonplaceholder.typicode.com/posts?userId=1

"""
parama = {
    "userId": 10
}
response = requests.get(url, params=parama)
print("Status Code:", response.status_code)
print(response.json())
"""

# post : 

"""import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "Python",
    "body": "Learning Requests Library",
    "userId": 1
}

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())
"""

# custom headers :
# Custom Headers Example
# Many websites block requests without a browser User-Agent.

"""
import requests

url = "https://httpbin.org/headers"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US"
}

response = requests.get(url, headers=headers)
print(response.json())
"""
#Cookies Example :
"""import requests

url = "https://httpbin.org/cookies"

cookies = {
    "username": "dishant"
}
response = requests.get(url, cookies=cookies)
print(response.json())
"""

# ex :1  it return default heading , The server returns the default headers sent by the requests library.
"""import requests

url = "https://httpbin.org/headers"
response = requests.get(url)
print(response.json())

"""

# ex :2 
'''import requests

url = "https://httpbin.org/headers"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US"
}
response = requests.get(url, headers=headers)
print(response.json())'''
"""
✅ You are not modifying a JSON file.
✅ You create a Python dictionary of headers.
✅ requests sends those headers with the HTTP request.
✅ The server receives them and, in the case of httpbin.org/headers, returns them as a JSON response so you can verify what was actually sent.
"""
"""
A cookie is a small piece of data that a website stores in your browser (or sends with requests) to remember information about you.
"""

"""import requests

url = "https://httpbin.org/cookies"
cookies = {
    "username": "Dishant"
}

response = requests.get(url, cookies=cookies)
print(response.json())
"""
#ex:2 
"""import requests

url = "https://httpbin.org/cookies"

cookies = {
    "username": "Dishant",
    "city": "Ahmedabad",
    "course": "Python"
}

response = requests.get(url, cookies=cookies)

print(response.json())
"""
import selenium
# print(selenium.__version__)

"""
webdriver allow you to automate browser interactions.
Python
↓
WebDriver
↓
Chrome
"""

# ex :1 
"""
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://example.com")

input("Press Enter to close...")
driver.quit()
"""

# ex :2  get page  title  

"""from selenium import webdriver
import time  

driver = webdriver.Chrome()
driver.get("https://example.com")

# time.sleep(3)
# print(driver.title)
driver.quit()
"""
# get  current url  : 
"""
print(driver.current_url)
"""

# HTML  code  : 
"""
print(driver.page_source) # print  500 character : driver.page_source[:500]
"""

# Finding Elements Find by Tag
"""
driver = driver.find_element("tag name", "h1")
print(driver.text)
"""
#Find by ID
# driver.find_element("id", "username")

#Find by Class
# driver.find_element("class name", "price")


# for  practice  using  flipkart  website  :
"""
flicart HTMl  code  is to much  long so  you can print the  first 500 character  using print(driver.page_source[:500]) 

"""
import time
import selenium
from selenium import webdriver

driver = webdriver.Chrome()  

driver.get("https://www.flipkart.com/")

time.sleep(5)

print("title :", driver.title)
print("current url :", driver.current_url)
print("page source :", driver.page_source[:500])


# pratical 1 : 
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://quotes.toscrape.com/js/")

WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "quote"))
)

quotes = driver.find_elements(By.CLASS_NAME, "quote")
for quote in quotes:
    text = quote.find_element(By.CLASS_NAME, "text").text
    author = quote.find_element(By.CLASS_NAME, "author").text

    print("Quote :", text)
    print("Author:", author)
    print("-" * 40)
driver.quit()
"""

# practical :2
"""from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org/")

time.sleep(2)  # Wait for the page to load

search = driver.find_element(By.ID, "searchInput")
search.send_keys("Python programming")
search.submit()

time.sleep(3)
print(driver.title)

driver.quit()
"""

