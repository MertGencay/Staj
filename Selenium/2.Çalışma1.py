from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.milliyet.com.tr/")

sleep(3)  # Sayfanın yüklenmesini bekliyorum

# Haber başlıklarını bul
basliklar = driver.find_elements(By.TAG_NAME, "h3")

print("Milliyet Haber Başlıkları:")
for baslik in basliklar[:10]:   # İlk 10 başlığı yazdır
    print("-", baslik.text)

driver.quit()
