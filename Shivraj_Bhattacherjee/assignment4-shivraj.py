# Assignment 4: Child Nodes Using CSS
# Identify and locate child/nested web elements using CSS selectors
# and interact with the required element.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Firefox()
try:
    driver.get("https://testautomationpractice.blogspot.com")
    driver.maximize_window()
    button = driver.find_element(By.CSS_SELECTOR, "div.dropdown > button.dropbtn")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
    ActionChains(driver).move_to_element(button).perform()
    time.sleep(1)
    laptop = driver.find_element(By.CSS_SELECTOR, "div.dropdown > div.dropdown-content > a:nth-child(2)")
    laptop.click()
    print("Successfully located and interacted with the child element using CSS child selector.")
finally:
    driver.quit()