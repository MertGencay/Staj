import pandas as pd

# CSV dosyasını oku
df = pd.read_csv(r"C:\Users\Mert\OneDrive\Masaüstü\Web Scraping\Pandas\ogrenciler.csv")

print("Ortalama not:", df["Not"].mean())
print("En yüksek not:", df["Not"].max())
print("En düşük not:", df["Not"].min())

# Kalan öğrenciler
kalanlar = df[df["Not"] < 50]
print("\nKalan öğrenciler:\n", kalanlar)

# Yeni CSV olarak kaydet
kalanlar.to_csv("kalan_ogrenciler.csv", index=False)
