from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import csv
import time, random
import pandas as pd

# ChromeDriver kurulumu
chromedriver_autoinstaller.install()

options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                     "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=options)
driver.get("https://arsiv.mackolik.com/Players/AllPlayers/Default.aspx")
time.sleep(random.uniform(4, 6))

data = []
page_count = 0
max_pages = 100

while page_count < max_pages:
    # Futbolcu satırlarını seç
    rows = driver.find_elements(By.CSS_SELECTOR, "#dvPlayerList table tbody tr[id^='row_']")
    for row in rows:
        cols = row.find_elements(By.TAG_NAME, "td")
        if len(cols) >= 9:
            row_data = [
                cols[0].text.strip(),  # Adı
                cols[1].text.strip(),  # Doğum Tarihi
                cols[2].text.strip(),  # Pozisyon
                cols[3].text.strip(),  # Son Takımı
                cols[4].text.strip(),  # Maç Sayısı
                cols[5].text.strip(),  # Gol Sayısı
                cols[6].text.strip(),  # Sarı Kart
                cols[8].text.strip()   # Kırmızı Kart
            ]
            if row_data[0] == "":
                row_data = row_data[1:]
            while len(row_data) < 8:
                row_data.append("")
            data.append(row_data)
        time.sleep(random.uniform(0.05, 0.2))

    # Sonraki sayfa butonuna tıkla
    try:
        next_btn = driver.find_element(By.CSS_SELECTOR, "#tblPlayers > tbody > tr:nth-child(22) > td > div > div.paging-box-left-temp > a:nth-child(13) > img")
        next_btn.click()
        time.sleep(random.uniform(3, 5))
        page_count += 1
    except:
        print("Daha fazla sayfa yok veya buton bulunamadı.")
        break

driver.quit()

# CSV dosyasına yazma
csv_file = "mackolik_futbolcular_100_sayfa.csv"
with open(csv_file, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Adı", "Doğum Tarihi", "Pozisyon", "Son Takımı",
                     "Maç Sayısı", "Gol Sayısı", "Sarı Kart", "Kırmızı Kart"])
    writer.writerows(data)

print(f"Toplam {len(data)} futbolcu CSV dosyasına yazıldı: '{csv_file}'")

# CSV'den HTML tablo oluşturma
df = pd.read_csv(csv_file)
html_table = df.to_html(index=False, classes="futbolcular-tablosu", border=0, escape=False)

html_content = f"""
<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<title>Mackolik Futbolcular</title>
<style>
    body {{
        font-family: Arial, sans-serif;
        background-color: #f5f5f5;
        padding: 20px;
    }}
    h1 {{
        text-align: center;
        color: #333;
    }}
    table.futbolcular-tablosu {{
        width: 100%;
        border-collapse: collapse;
        margin: 20px auto;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        background-color: #fff;
    }}
    table.futbolcular-tablosu th, table.futbolcular-tablosu td {{
        padding: 10px 12px;
        text-align: center;
        border-bottom: 1px solid #ddd;
    }}
    table.futbolcular-tablosu th {{
        background-color: #0077cc;
        color: #fff;
        text-transform: uppercase;
    }}
    table.futbolcular-tablosu tr:hover {{
        background-color: #f1f1f1;
    }}
</style>
</head>
<body>
<h1>Mackolik Futbolcular Listesi</h1>
{html_table}
</body>
</html>
"""

html_file = "mackolik_futbolcular.html"
with open(html_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"HTML tablosu '{html_file}' olarak kaydedildi.")
