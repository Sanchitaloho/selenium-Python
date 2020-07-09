from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://classic.crmpro.com/")

#can also find all links
allLinks = driver.find_elements(By.TAG_NAME, 'a')
print(len(allLinks))
for ele in allLinks:
    linksText = ele.text
    print(ele.get_attribute('src'))

header_element = driver.find_element(By.TAG_NAME, 'h1')
print(header_element.text)
print(driver.title)

username = driver.find_element(By.NAME, 'username')
password = driver.find_element(By.NAME, 'password')
login_button = driver.find_element(By.XPATH, "//input[@value='Login']")

username.send_keys("batchautomation")
password.send_keys("Test@12345")
login_button.click()

driver.get("https://app.hubspot.com/login")

driver.find_element(By.CSS_SELECTOR, '#username').send_keys("san2@gmail.com")
driver.find_element(By.CLASS_NAME, 'login-password').send_keys("test@123")
driver.find_element(By.CLASS_NAME, 'login-submit').click()
driver.find_element(By.CSS_SELECTOR, 'input.form-control.private-form__control.login-email').send_keys("test@gmail.com")
driver.find_element(By.XPATH, "//input[@class='form-control private-form__control login-email']").send_keys("test@gmail.com")

driver.find_element(By.CLASS_NAME, 'form-control private-form__control login-email').send_keys("test@gmail.com")
driver.find_element(By.LINK_TEXT, 'Sign up').click()
driver.find_element(By.PARTIAL_LINK_TEXT, 'Sign').click()
driver.find_element(By.CLASS_NAME, 'login-submit').click()

