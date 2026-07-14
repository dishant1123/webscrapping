"""
1. Fetch Posts from a Free API (GET Request) : using https://jsonplaceholder.typicode.com/posts
2. Print Only First Post
3. Print All Titles
4. Store API Data into CSV
5. API ==> weather api  :https://api.open-meteo.com/v1/forecast?latitude=23.03&longitude=72.58&current_weather=true

"""
# ex :1 
import requests
import pandas as pd 

"""url= "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url) 
data = response.json()
print(response.status_code)
# print(data)
print("title : ",data[3]['title'])
print("body : ",data[3]['body'])

df =pd.DataFrame(data)
df.to_csv("posts.csv",index=False)
print(df.head())
"""

# post : url 
"""
url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

new_data = {
    "userId": 1000,
    "title": "python",
    "body": "i am  using python daily"
    
}
response =requests.post(url, json=new_data)
print(response.status_code)
print(response.json())
"""
# weather api : 

"""url ="https://api.open-meteo.com/v1/forecast?latitude=23.03&longitude=72.58&current_weather=true"

response = requests.get(url)
data = response.json()

print(response.status_code)
print("temprature  : ",data['current_weather']['temperature'])  
"""
