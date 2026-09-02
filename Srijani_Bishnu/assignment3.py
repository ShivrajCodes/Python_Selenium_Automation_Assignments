#CSS Selector Challenge : including selectors with wildcards
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

browsername="chrome"

if browsername.lower()=="chrome":
    driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
elif browsername.lower()=="firefox":
    driver=webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
else:
    raise Exception("Invalid browser name. Please choose 'chrome' or 'firefox'.")

driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()

#Selecting elements using locator

driver.find_element(By.CSS_SELETOR, "input#name").send_keys("Test_name") #id = name
driver.find_element(By.CSS_SELECTOR, "input#name").send_keys("Test_name") #id = name
driver.find_element(By.CSS_SELECTOR, ".form-control").send_keys("Test_name") #class = form-control

#Selecting elements using wildcards

#^:starts with

elements=driver.find_elements(By.CSS_SELECTOR, "input[id^='input']")

for element in elements:
    element.send_keys("test_value")

#*:contains

elements=driver.find_elements(By.CSS_SELECTOR, "input[id*='input']")

for element in elements:
    element.send_keys("test_value")

#$:ends with

elements=driver.find_elements(By.CSS_SELECTOR, "input[id$='day']")

for element in elements:
    element.click()

time.sleep(5)

driver.quit()