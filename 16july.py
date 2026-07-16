"https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"

import selenium 
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
driver = webdriver.Chrome()

driver.get("https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops")
driver.maximize_window()

webdriver_wait = WebDriverWait(driver, 10)
webdriver_wait.until(
    EC.presence_of_all_elements_located(
        (By.CLASS_NAME, "thumbnail")
    )
)
name =[]
price =[]
rating =[]

products = driver.find_elements(By.CLASS_NAME, "thumbnail") 

for  product in products:
    name.append(
        product.find_element(
            By.CLASS_NAME,
            "title"
        ).get_attribute("title")
    )
    
    price.append(
        product.find_element(
            By.CLASS_NAME,
            "price"
        ).text
    )

    rating.append(
        len(product.find_elements(
            By.CSS_SELECTOR,
            ".ratings span.ws-icon-star"
        ))
    )
driver.quit()

df = pd.DataFrame({
    "Laptop Name": name,
    "Price": price,
    "Rating": rating
})

df.to_csv("laptops_cleaned.csv",index=False)
print(df)