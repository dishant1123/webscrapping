import selenium
from selenium import webdriver
import  time 
# ex :1 

"""driver = webdriver.Chrome()
driver.get("https://quotes.toscrape.com/js/")
input("Press Enter to close...")
driver.quit()
"""
# ex:2 

driver = webdriver.Chrome()
driver.get("https://quotes.toscrape.com/js/")

# driver.get("https://www.amazon.com")

time.sleep(3)
print(driver.current_url)
print(driver.title)
# print(driver.page_source())

driver.quit()