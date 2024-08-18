from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_Opt=webdriver.ChromeOptions()
chrome_Opt.add_experimental_option(name="detach",value=True)
driver=webdriver.Chrome()
driver.get("https://www.python.org/")
values=driver.find_elements(By.CSS_SELECTOR,value=".event-widget time")
names=driver.find_elements(By.CSS_SELECTOR,value=".event-widget a")
for val in names:
    print(val.text)