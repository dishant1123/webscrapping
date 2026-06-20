"""
webscraping  :

1.static  : HTML  
2. dynamic : JS  ===>API 

# lib :: requests , beautifulsoup : 

"""
import  requests
from bs4 import BeautifulSoup
# ex:1 
'''
html = """
<h1>STUDENTS </h1>
<p>my name is  dishant. i am a student</p>
<title>INTRODUCTION</title>

"""
soup = BeautifulSoup(html,"html.parser") 
h1_tag = soup.find("h1")
title = soup.find("title")
p_tag = soup.find("p")

print(h1_tag.text)
print(title.text)
print(p_tag.text)
'''
# ex:2 
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
soup = BeautifulSoup(html, "html.parser")

title = soup.find("title")
h1_tag = soup.find("h1")
p_tag = soup.find("p")
div_tag = soup.find("div")
link_tag = soup.find("a")['href']

ul_tag = soup.find_all("ul")

print(title.text)
print(h1_tag.text)
print(p_tag.text)
print(div_tag.text)
print(link_tag)


for i in soup.find_all("li"):
    print(i.text)
