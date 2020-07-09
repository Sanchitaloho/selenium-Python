from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import time

browser_name = "firefox"
if browser_name == "chrome":

    driver = webdriver.Chrome(ChromeDriverManager().install())

elif browser_name == "firefox":

    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif browser_name == "safari":
    driver = webdriver.Safari()
else:
    print("Please pass the correct browser name : " + browser_name)
    raise Exception('driver is not found')

driver.implicitly_wait(10)
driver.get("https://app.hubspot.com/login")

driver.find_element(By.ID, 'username').send_keys('sanch.loho28@gmail.com')
driver.find_element(By.ID, 'password').send_keys('Autotest@1234')
driver.find_element(By.ID, 'loginBtn').click()