from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

# 5 adet buton ekle
add_button = driver.find_element(By.CSS_SELECTOR, "button[onclick='addElement()']")
for _ in range(5):
    add_button.click()
    time.sleep(0.2)

# Eklenen butonları çek
buttons = driver.find_elements(By.CLASS_NAME, "added-manually")
print(f"{len(buttons)} adet buton eklendi.")

driver.quit()
