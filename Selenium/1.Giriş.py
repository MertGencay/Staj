from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options
from time import sleep

# ChromeDriver otomatik yükle
chromedriver_autoinstaller.install()

# Logları kapatma ayarı
chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])  # Gereksiz logları kapat

# Chrome başlat
driver = webdriver.Chrome(options=chrome_options)

url = "https://tr.wikipedia.org/"
driver.get(url)
sleep(3)
driver.maximize_window()
sleep(3)
# driver.save_screenshot("ekrangoruntusu.png")
# sleep(3)
driver.minimize_window()
sleep(3)
driver.maximize_window()
sleep(3)
url = "https://www.youtube.com/"
driver.get(url)
sleep(3)
driver.back()
sleep(3)
driver.forward()
sleep(3)
driver.refresh()
sleep(3)
driver.quit()
