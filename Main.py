from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome()
driver.get("https://www.python.org/")
value_Checked=driver.find_element(By.NAME,value="q")
print(value_Checked.get_attribute("placeholder"))
#button=driver.find_element(By.id,value="submit")
#print(button.size)
xpath=driver.find_element(By.XPATH,value='//*[@id="content"]/div/section/div[1]/div[1]/h2')
print(xpath.text)
driver.quit()