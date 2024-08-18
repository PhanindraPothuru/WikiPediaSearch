from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_Opt=webdriver.ChromeOptions()
chrome_Opt.add_experimental_option("detach",True)
driver=webdriver.Chrome()
driver.get("http://secure-retreat-92358.herokuapp.com/")
f_name=driver.find_element(By.NAME,value="fName")
f_name.send_keys("Phani")
l_name=driver.find_element(By.NAME,value="lName")
l_name.send_keys("Cherry")
Email_name=driver.find_element(By.NAME,value="email")
Email_name.send_keys("phanipothuru67@gmail.com")
Email_name.send_keys(Keys.TAB)
driver.quit()