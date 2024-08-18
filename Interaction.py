from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_Opt=webdriver.ChromeOptions()
chrome_Opt.add_experimental_option(name="detach",value=True)
driver=webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")
vale=driver.find_element(By.XPATH,value='//*[@id="articlecount"]/a[1]')
print(vale.text)
#vale.click()
#click_Value=driver.find_element(By.LINK_TEXT,value="By email")

search=driver.find_element(By.NAME,value="search")
search.send_keys("Python")
#driver.quit()