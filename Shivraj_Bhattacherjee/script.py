# Assignment 4: Child Nodes Using CSS
# Identify and locate child/nested web elements using CSS selectors
# and interact with the required element.
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

try:
    driver.get("https://testautomationpractice.blogspot.com")
    button = driver.find_element(By.XPATH, "//button[normalize-space()='Point Me']")
    parent = button.find_element(By.XPATH, "./..")
    print(parent.get_attribute("outerHTML"))
finally:
    driver.quit()
