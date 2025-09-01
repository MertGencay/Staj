import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Bu grafikler maçkolik sitesinden en golcü 2000 oyuncunun verisinin çekilmesiyle oluşturulmuştur.

# CSV dosyasını okuma
df = pd.read_csv(r"C:\Users\Mert\OneDrive\Masaüstü\Web Scraping\Projeler\FutbolcuBilgileri\mackolik_futbolcular_100_sayfa.csv")

# Tip dönüşümleri
df['Maç Sayısı'] = df['Maç Sayısı'].astype(int)
df['Gol Sayısı'] = df['Gol Sayısı'].astype(int)
df['Sarı Kart'] = df['Sarı Kart'].astype(int)

# 1. En golcü 10 oyuncu (Bar Grafiği)
en_golcu = df.nlargest(10, "Gol Sayısı")
plt.figure(figsize=(10,6))
plt.barh(en_golcu['Adı'], en_golcu['Gol Sayısı'], color='orange')
plt.xlabel("Gol Sayısı")
plt.title("En Golcü 10 Futbolcu")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("en_golcu_10.png", dpi=150)
plt.show()

# 2. Pozisyon dağılımı (Pasta Grafiği)
pozisyon_sayilari = df['Pozisyon'].value_counts()
plt.figure(figsize=(6,6))
plt.pie(pozisyon_sayilari, labels=pozisyon_sayilari.index, autopct='%1.1f%%', startangle=90, colors=['skyblue','lightgreen','salmon'])
plt.title("Pozisyon Dağılımı")
plt.tight_layout()
plt.savefig("pozisyon_dagilimi.png", dpi=150)
plt.show()

# 3. Sarı kart dağılımı (Histogram)
plt.figure(figsize=(10,6))
plt.hist(df['Sarı Kart'], bins=20, color='yellow', edgecolor='black')
plt.xlabel("Sarı Kart Sayısı")
plt.ylabel("Futbolcu Sayısı")
plt.title("Sarı Kart Dağılımı")
plt.tight_layout()
plt.savefig("sari_kart_dagilimi.png", dpi=150)
plt.show()

# 4. Maç sayısına göre gol sayısı (Scatter/Nokta Grafiği)
plt.figure(figsize=(10,6))
plt.scatter(df['Maç Sayısı'], df['Gol Sayısı'], color='red', alpha=0.6)
plt.xlabel("Maç Sayısı")
plt.ylabel("Gol Sayısı")
plt.title("Maç Sayısına Göre Gol Sayısı")
plt.tight_layout()
plt.savefig("mac_gol_scatter.png", dpi=150)
plt.show()

# Yaş hesaplama
current_year = datetime.now().year
df['Yaş'] = current_year - df['Doğum Tarihi'].astype(int)
df['Yaş'] = df['Yaş'].clip(lower=25, upper=50)

# 5. Yaş dağılımı (Histogram)
plt.figure(figsize=(10,6))
plt.hist(df['Yaş'], bins=range(25, 51), color='skyblue', edgecolor='black', align='left')
plt.xlabel("Yaş")
plt.ylabel("Futbolcu Sayısı")
plt.title("Futbolcuların Yaş Dağılımı (25-50)")
plt.xticks(range(25, 51))
plt.tight_layout()
plt.savefig("yas_dagilimi.png", dpi=150)
plt.show()

# 6. Takım bazlı dağılım (İlk 10 takım)
takim_sayisi = df['Son Takımı'].value_counts().nlargest(10)
plt.figure(figsize=(12,6))
takim_sayisi.plot(kind='bar', color='skyblue')
plt.title("En Çok Futbolcusu Olan İlk 10 Takım")
plt.xlabel("Takım")
plt.ylabel("Futbolcu Sayısı")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("takim_dagilimi.png", dpi=150)
plt.show()
