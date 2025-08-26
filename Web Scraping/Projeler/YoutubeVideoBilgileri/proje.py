from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import chromedriver_autoinstaller
import os
import sys
from colorama import Fore, Style, init

# Colorama'yı başlat
init(autoreset=True)

# Hata mesajlarını gizle
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
sys.stderr = open(os.devnull, 'w')

# ChromeDriver otomatik kurulum
chromedriver_autoinstaller.install()

# Kullanıcıdan YouTube URL'si al
url = input("Bilgi çekmek istediğiniz YouTube videosunun URL'sini girin: ")

driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)

# Verileri çek
title = driver.find_element(By.XPATH,'//*[@id="title"]/h1/yt-formatted-string').text
view_count = driver.find_element(By.XPATH,'//*[@id="info"]/span[1]').text
like_count = driver.find_element(By.XPATH,'//*[@id="top-level-buttons-computed"]/segmented-like-dislike-button-view-model/yt-smartimation/div/div/like-button-view-model/toggle-button-view-model/button-view-model/button/div[2]').text
upload_date = driver.find_element(By.XPATH,'//*[@id="info"]/span[3]').text
channel_name = driver.find_element(By.XPATH,'//*[@id="text"]/a').text
subscriber_count = driver.find_element(By.XPATH,'//*[@id="owner-sub-count"]').text

# Renkli çıktı
print("\n" + Fore.YELLOW + "="*55)
print(Fore.CYAN + f"📌 Başlık: {Fore.WHITE}{title}")
print(Fore.MAGENTA + f"👁‍🗨 Görüntülenme Sayısı: {Fore.WHITE}{view_count}")
print(Fore.GREEN + f"👍 Beğeni Sayısı: {Fore.WHITE}{like_count}")
print(Fore.BLUE + f"📅 Yüklenme Tarihi: {Fore.WHITE}{upload_date}")
print(Fore.RED + f"📺 Kanal Adı: {Fore.WHITE}{channel_name}")
print(Fore.LIGHTYELLOW_EX + f"👥 Abone Sayısı: {Fore.WHITE}{subscriber_count}")
print(Fore.YELLOW + "="*55 + "\n" + Style.RESET_ALL)

time.sleep(3)
driver.quit()
