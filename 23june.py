import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com" 

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# title_tag = soup.find("title")
# h1_tag = soup.find("h1")
# h2_tag = soup.find("h2")
# p_tag = soup.find("p")
# div_tag = soup.find("div")
# tages = soup.find_all("span",class_="tag-item")
# link_tag = soup.find("a")['href']

# print("Title:", title_tag.text)
# print("Heading:", h1_tag.text)
# print("Heading:1", h2_tag.text)
# print("Paragraph:", p_tag.text)
# print("Div:", div_tag.text[:200])
# print("Tags:", tages.text)
"""
for i in soup.find_all("span",class_="tag-item"):
    print(i.text)
    
for j in soup.find_all("a"):
    print(j.text)"""
    
authors = soup.find_all("small",class_="author")
"""
for  x in range(len(authors)):
    print(authors[x].text)
"""    
"""all_tages = soup.find_all("div",class_="tags")
for  y in range(len(all_tages)):
    print(all_tages[y].text)
"""

# 1 quotes print : 

first=soup.find_all("span",class_="text")
print(first[0].text)

# for i in range(len(first_quotes)):  # first_
    # print(first_quotes[i].text)