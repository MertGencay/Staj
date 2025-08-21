# Alibaba Web Scraping Tedarikçi Listesi
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

# Chrome seçenekleri
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
)

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

def shorten(text, max_len=50):
    return text if len(text) <= max_len else text[:max_len-3] + "..."

def scrape_alibaba(keyword, max_pages=5):
    """Belirtilen anahtar kelime ve sayfa sayısı kadar veri çeker."""
    urunler = []
    for page in range(1, max_pages+1):
        url = f"https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText={keyword}&page={page}"
        driver.get(url)

        wait = WebDriverWait(driver, 20)
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.m-gallery-product-item-v2")))
        time.sleep(2)

        products = driver.find_elements(By.CSS_SELECTOR, "div.m-gallery-product-item-v2")

        for product in products:
            name = shorten(product.find_element(By.CSS_SELECTOR, "h2.search-card-e-title a span").text) if product.find_elements(By.CSS_SELECTOR, "h2.search-card-e-title a span") else ""
            price = product.find_element(By.CSS_SELECTOR, "div.search-card-e-price-main").text if product.find_elements(By.CSS_SELECTOR, "div.search-card-e-price-main") else ""
            seller = shorten(product.find_element(By.CSS_SELECTOR, "a.search-card-e-company").text, 30) if product.find_elements(By.CSS_SELECTOR, "a.search-card-e-company") else ""
            moq = product.find_element(By.CSS_SELECTOR, "div[data-aplus-auto-card-mod*='moq']").text if product.find_elements(By.CSS_SELECTOR, "div[data-aplus-auto-card-mod*='moq']") else ""

            urunler.append({
                "Kategori": keyword,
                "Ürün Adı": name,
                "Fiyat": price,
                "Satıcı": seller,
                "Minimum Sipariş": moq
            })
    return urunler

try:
    categories = ["electronics", "textile", "apparel", "furniture", "home-garden", "beauty", "sports", "toys"]
    all_data = []

    for cat in categories:
        print(f"{cat} kategorisi için veri çekiliyor...")
        all_data.extend(scrape_alibaba(cat, max_pages=5)) # Her kategori için 5 sayfa

    df = pd.DataFrame(all_data)

    # CSV KAYIT
    df.to_csv("alibaba_multi_category.csv", index=False, encoding="utf-8-sig")
    print("\nTüm veriler 'alibaba_multi_category.csv' dosyasına kaydedildi.")

finally:
    driver.quit()

# --- Sekmeli HTML OLUŞTURMA ---
html_content = f"""
<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<title>Alibaba Ürün Listesi</title>
<style>
body {{ font-family: Arial, sans-serif; background-color: #f4f4f4; padding: 20px; }}
h1 {{ text-align: center; color: #333; }}
/* Sekme butonları */
.tab {{
  overflow: hidden;
  border-bottom: 1px solid #ccc;
  background-color: #f1f1f1;
}}
.tab button {{
  background-color: inherit;
  float: left;
  border: none;
  outline: none;
  cursor: pointer;
  padding: 10px 20px;
  transition: 0.3s;
  font-size: 16px;
}}
.tab button:hover {{ background-color: #ddd; }}
.tab button.active {{ background-color: #ccc; }}
.tabcontent {{
  display: none;
  padding: 10px 0;
}}
table {{
  border-collapse: collapse;
  width: 95%;
  margin: 10px auto 30px auto;
  background: white;
  box-shadow: 0px 4px 8px rgba(0,0,0,0.1);
  border-radius: 10px;
  overflow: hidden;
}}
th, td {{
  border: 1px solid #ddd;
  padding: 12px 15px;
  text-align: left;
}}
th {{
  background-color: #4CAF50;
  color: white;
  font-weight: bold;
}}
tr:nth-child(even) {{ background-color: #f9f9f9; }}
tr:hover {{ background-color: #f1f1f1; }}
</style>
</head>
<body>
<h1>Alibaba Ürün Listesi</h1>

<div class="tab">
"""
# Tab butonları
for i, cat in enumerate(categories):
    active = "active" if i==0 else ""
    html_content += f'<button class="tablinks {active}" onclick="openTab(event, \'{cat}\')">{cat}</button>'
html_content += "</div>"

# Tab içerikleri
for i, cat in enumerate(categories):
    display = "block" if i==0 else "none"
    html_content += f'<div id="{cat}" class="tabcontent" style="display:{display}"><table><thead><tr>'
    html_content += ''.join(f"<th>{col}</th>" for col in df.columns)
    html_content += "</tr></thead><tbody>"

    cat_df = df[df["Kategori"]==cat]
    for _, row in cat_df.iterrows():
        html_content += "<tr>"
        for col in df.columns:
            html_content += f"<td>{row[col]}</td>"
        html_content += "</tr>"
    html_content += "</tbody></table></div>"

# JS ile sekme fonksiyonu
html_content += """
<script>
function openTab(evt, categoryName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) { tabcontent[i].style.display = "none"; }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) { tablinks[i].className = tablinks[i].className.replace(" active", ""); }
  document.getElementById(categoryName).style.display = "block";
  evt.currentTarget.className += " active";
}
</script>
</body>
</html>
"""

with open("alibaba_products_tabs.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("\nSekmeli HTML dosyası oluşturuldu: alibaba_products_tabs.html")
