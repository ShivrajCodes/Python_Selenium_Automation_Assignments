from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# 1. Locate element using ID
name_box = driver.find_element(By.ID, "name")
name_box.send_keys("Roney")


# 2. Locate element using NAME
gender = driver.find_element(By.NAME, "gender")
gender.click()


# 3. Locate element using TAG_NAME
heading = driver.find_element(By.TAG_NAME, "h1")
print("Heading:", heading.text)


# 4. Locate element using LINK_TEXT
home_link = driver.find_element(By.LINK_TEXT, "Home")
print("Home link text:", home_link.text)


# 5. Locate element using CLASS_NAME
# Finds one element having the class 'form-control'
element = driver.find_element(By.CLASS_NAME, "form-control")
print("Element located using class name:", element.get_attribute("id"))


time.sleep(5)

driver.quit()