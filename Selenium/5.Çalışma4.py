from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/checkboxes")

time.sleep(2)

checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
for box in checkboxes:
    if not box.is_selected():  # İşaretli değilse işaretle
        box.click()

print("Tüm checkbox'lar işaretlendi.")
driver.quit()
