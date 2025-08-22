from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

# Chrome seçenekleri
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

def scrape_category(category_name, base_url, max_pages=3):
    """Verilen kategori için belirtilen sayfa sayısını scrape eder"""
    records = []
    for page in range(1, max_pages + 1):
        url = f"{base_url}?page={page}"
        driver.get(url)
        wait = WebDriverWait(driver, 30)

        book_selector = ".facet__products-list.js-facet-product-list > div"
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, book_selector)))
        books = driver.find_elements(By.CSS_SELECTOR, book_selector)

        for book in books:
            # Kitap adı + yazar
            title_links = book.find_elements(By.CSS_SELECTOR, ".prd-infos a")
            title_author = " - ".join([a.text.strip() for a in title_links])
            link = title_links[0].get_attribute("href").strip() if title_links else ""

            # Fiyat: indirimli varsa ikinci span, yoksa normal fiyat
            price_text = "Fiyat yok"
            discount_spans = book.find_elements(By.CSS_SELECTOR, ".prd-container-campaign .campaign-price span")
            if discount_spans and len(discount_spans) > 1:
                price_text = discount_spans[1].text.strip()
            else:
                normal_elem = book.find_elements(By.CSS_SELECTOR, ".prd-price-wrapper div div div")
                if normal_elem and normal_elem[0].text.strip():
                    price_text = normal_elem[0].text.strip()

            records.append({
                "Kategori": category_name,
                "Kitap Adı ve Yazar": title_author,
                "Fiyat": price_text,
                "Link": link
            })

        # Random sleep ile ban riskini azalt
        time.sleep(random.uniform(2, 5))

    return records

try:
    # Güncel kategoriler ve URL’leri
    categories = {
        "Polisiye": "https://www.dr.com.tr/kategori/Kitap/Edebiyat/Roman/Polisiye/grupno=00497",
        "Çocuk": "https://www.dr.com.tr/kategori/kitap/cocuk-ve-genclik/grupno=00884",
        "Tarih": "https://www.dr.com.tr/kategori/Kitap/Arastirma-Tarih/grupno=00051",
        "Bilim Kurgu": "https://www.dr.com.tr/kategori/Kitap/Edebiyat/Roman/Bilim-Kurgu/grupno=00254"
    }

    all_data = []
    for cat_name, url in categories.items():
        print(f"{cat_name} kategorisi çekiliyor...")
        all_data.extend(scrape_category(cat_name, url, max_pages=3))

    df = pd.DataFrame(all_data)

    # CSV kaydet
    df.to_csv("kitaplar_multi_category_3pages.csv", index=False, encoding="utf-8-sig")

    # Sekmeli HTML oluştur
    html_content = f"""
    <!DOCTYPE html>
    <html lang="tr">
    <head>
    <meta charset="UTF-8">
    <title>Kitap Listesi</title>
    <style>
    body {{ font-family: Arial, sans-serif; padding: 20px; background: #f4f4f4; }}
    h1 {{ text-align: center; color: #333; }}
    .tab {{ overflow: hidden; border-bottom: 1px solid #ccc; background-color: #f1f1f1; }}
    .tab button {{
      background-color: inherit; float: left; border: none; outline: none;
      cursor: pointer; padding: 10px 20px; transition: 0.3s; font-size: 16px;
    }}
    .tab button:hover {{ background-color: #ddd; }}
    .tab button.active {{ background-color: #ccc; }}
    .tabcontent {{ display: none; padding: 10px 0; }}
    table {{ border-collapse: collapse; width: 95%; margin: 10px auto 30px auto; background: white;
             box-shadow: 0px 4px 8px rgba(0,0,0,0.1); border-radius: 10px; overflow: hidden; }}
    th, td {{ border: 1px solid #ddd; padding: 12px 15px; text-align: left; }}
    th {{ background-color: #4CAF50; color: white; font-weight: bold; }}
    tr:nth-child(even) {{ background-color: #f9f9f9; }}
    tr:hover {{ background-color: #f1f1f1; }}
    a {{ text-decoration: none; color: #1a73e8; }}
    </style>
    </head>
    <body>
    <h1>Kitap Listesi</h1>

    <div class="tab">
    """
    # Sekme butonları
    for i, cat in enumerate(categories.keys()):
        active = "active" if i==0 else ""
        html_content += f'<button class="tablinks {active}" onclick="openTab(event, \'{cat}\')">{cat}</button>'
    html_content += "</div>"

    # Tab içerikleri
    for i, cat in enumerate(categories.keys()):
        display = "block" if i==0 else "none"
        html_content += f'<div id="{cat}" class="tabcontent" style="display:{display}"><table><thead><tr>'
        html_content += ''.join(f"<th>{col}</th>" for col in df.columns if col != "Kategori")
        html_content += "</tr></thead><tbody>"
        cat_df = df[df["Kategori"]==cat]
        for _, row in cat_df.iterrows():
            html_content += "<tr>"
            for col in df.columns:
                if col != "Kategori":
                    if col == "Link":
                        html_content += f'<td><a href="{row[col]}" target="_blank">Tıkla</a></td>'
                    else:
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

    with open("kitaplar_multi_category_3pages.html", "w", encoding="utf-8") as f:
        f.write(html_content)

finally:
    driver.quit()
