#Q2 MuULTIPLE ELEMENT IDENTIFICATION USING PYTHON AND SELENIUM
#https://rahulshettyacademy.com/AutomationPractice/
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(2)

links = driver.find_elements(By.TAG_NAME, "a")

print(f"Total number of links found on the page: {len(links)}")
print("-" * 50)

for index, link in enumerate(links, start=1):
    link_text = link.text.strip()
    if link_text:
        print(f"Link {index}: {link_text}")
    else:
        print(f"Link {index}: [No visible text - possibly an icon/image link]")

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print("-" * 50)
print(f"Total number of checkboxes found: {len(checkboxes)}")

time.sleep(3)
driver.quit()