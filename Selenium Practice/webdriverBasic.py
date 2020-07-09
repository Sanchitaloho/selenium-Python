from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\\Sanchita\\learning\\chromedriver_win32\\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("http://www.google.com")
print(driver.title)
driver.find_element(By.NAME,'q').send_keys("automation labs")
optionList = driver.find_elements(By.CSS_SELECTOR, 'ul.erkvQe li span')
print("length", len(optionList))

for ele in optionList:
    print(ele.text)
    if ele.text == 'lab services automation':
        ele.click()
        break


time.sleep(5)
driver.quit()