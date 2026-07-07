import selenium
from selenium import webdriver
import  time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# ex :1 

"""driver = webdriver.Chrome()
driver.get("https://quotes.toscrape.com/js/")
input("Press Enter to close...")
driver.quit()
"""
# ex:2 

"""driver = webdriver.Chrome()
driver.get("https://quotes.toscrape.com/js/")

# driver.get("https://www.amazon.com")

time.sleep(3)
print(driver.current_url)
print(driver.title)
print(driver.page_source[:500])

driver.quit()
"""
# !pip install selenium

#ex:3

driver = webdriver.Chrome()
driver.get("https://quotes.toscrape.com/js/")

WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "quote"))
)

quotes = driver.find_elements(By.CLASS_NAME, "quote")

for i in quotes:
    text =i.find_element(By.CLASS_NAME, "text").text
    author = i.find_element(By.CLASS_NAME, "author").text
    print(text)
    print(author)
    print("-" * 40)
    
driver.quit()
