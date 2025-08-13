from bs4 import BeautifulSoup

html_doc = """
<html>
<head><title>Test Sayfası</title></head>
<body>
<h1>Merhaba Dünya</h1>
<p class="yazi">Bu bir paragraf.</p>
<p class="yazi">Bu ikinci paragraf.</p>
<ul>
    <li>Python</li>
    <li>JavaScript</li>
    <li>HTML</li>
</ul>
<a href="https://example.com">Example Link</a>
<a href="https://google.com" target="_blank">Google</a>
</body>
</html>
"""

# HTML'yi parse et
soup = BeautifulSoup(html_doc, "html.parser")

# 1. Başlık (title) ve başlık içeriği
print("Sayfa başlığı:", soup.title.text)

# 2. İlk H1 etiketi
print("Başlık:", soup.h1.text)

# 3. Tüm paragrafları listeleme
print("\nParagraflar:")
for p in soup.find_all("p"):
    print("-", p.text)

# 4. Class ile filtreleme
yazi_paragraflari = soup.find_all("p", class_="yazi")
print("\n'yazi' class'ına sahip paragraflar:")
for p in yazi_paragraflari:
    print("-", p.text)

# 5. Liste elemanlarını (li) çekme
print("\nListe elemanları:")
for li in soup.find_all("li"):
    print("-", li.text)

# 6. Tüm linkleri (a) çekme
print("\nLinkler:")
for a in soup.find_all("a"):
    print("-", a.text, "->", a["href"])

# 7. CSS seçici ile arama
print("\nCSS seçici ile (ul > li) bulma:")
for item in soup.select("ul > li"):
    print("-", item.text)

# 8. İlk paragrafın üst elementini bulma
print("\nİlk paragrafın parent etiketi:", soup.p.parent.name)

# 9. İkinci linkin attribute bilgileri
ikinci_link = soup.find_all("a")[1]
print("\nİkinci link attribute'ları:", ikinci_link.attrs)
