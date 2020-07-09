from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")


def select_values(element, value):
    select = Select(element)
    select.select_by_visible_text(value)


def select_values_from_dropdown(dropDownOptionsList, value):
    print(len(dropDownOptionsList))
    for ele in dropDownOptionsList:
        print(ele.text)
        if ele.text == value:
            ele.click()
            break


indus_options = driver.find_elements(By.XPATH, '//select[@id="Form_submitForm_Industry"]/option')
country_options = driver.find_elements(By.XPATH, '//select[@id="Form_submitForm_Country"]/option')

select_values_from_dropdown(indus_options, 'Education')
select_values_from_dropdown(indus_options, 'Travel')
select_values_from_dropdown(country_options, 'India')

ele_indus = driver.find_element(By.ID, 'Form_submitForm_Industry')
ele_country = driver.find_element(By.ID, 'Form_submitForm_Country')

select_values(ele_indus, 'Education')
select_values(ele_country, 'India')

select = Select(ele_indus)
IndustryList = select.options

#no need to call the methods again and again
#select.select_by_visible_text('Education')
#select.select_by_index(4)
#select.select_by_value('health')

#print(select.is_multiple)

#select_con = Select(ele_country)
#select_con.select_by_visible_text('India')

driver.quit()