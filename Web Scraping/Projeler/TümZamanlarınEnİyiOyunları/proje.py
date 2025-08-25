from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pandas as pd

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
games = []

for page in range(1, 101): 
    url = f"https://www.metacritic.com/browse/game/?releaseYearMin=1958&releaseYearMax=2025&page={page}"
    driver.get(url)

    # Sayfanın yüklenmesini bekler
    wait.until(EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, ".c-finderProductCard_title h3 > span:nth-child(2)")
    ))

    # Sayfayı aşağı kaydırarak lazy load'u tetikler
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(2)

    # Oyun isimlerini ve skorları alır
    game_names = driver.find_elements(By.CSS_SELECTOR, ".c-finderProductCard_title h3 > span:nth-child(2)")
    metascores = driver.find_elements(By.CSS_SELECTOR, ".c-finderProductCard_score span div div")

    for name, score in zip(game_names, metascores):
        game_text = name.get_attribute("innerHTML").strip()
        score_text = score.text.strip()

        games.append({
            "Page": page,
            "Game": game_text,
            "Metascore": score_text
        })

    sleep(1)

driver.quit()

# DataFrame oluştur
df = pd.DataFrame(games)

# CSV kaydet
df.to_csv("bestgames.csv", index=False)

# HTML olarak kaydet (güzel tablo ile)
html_content = df.to_html(index=False, classes="table table-striped table-bordered", border=0)

# Basit CSS ekleyelim
html_style = """
<style>
.table {width: 100%; border-collapse: collapse; font-family: Arial, sans-serif;}
.table th, .table td {border: 1px solid #ddd; padding: 8px; text-align: left;}
.table th {background-color: #4CAF50; color: white;}
.table tr:nth-child(even){background-color: #f2f2f2;}
.table tr:hover {background-color: #ddd;}
</style>
"""

with open("bestgames.html", "w", encoding="utf-8") as f:
    f.write(html_style + html_content)

print(f"{len(df)} oyun çekildi ve HTML tablosu oluşturuldu.")
