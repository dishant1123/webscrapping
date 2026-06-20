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

soup = BeautifulSoup(html, "html.parser")

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