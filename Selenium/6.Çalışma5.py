from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

time.sleep(2)

# Kullanıcı adı ve şifre gir
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

# Giriş butonuna tıkla
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(2)

# Başarı mesajını al
message = driver.find_element(By.ID, "flash").text
print("Mesaj:", message)

driver.quit()
