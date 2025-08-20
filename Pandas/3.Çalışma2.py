import pandas as pd

df = pd.read_csv(r"C:\Users\Mert\OneDrive\Masaüstü\Web Scraping\Pandas\satislar.csv")

# Yeni sütun: Ciro
df["Ciro"] = df["Fiyat"] * df["Adet"]

print("Toplam Ciro:", df["Ciro"].sum())
print("\nEn çok satan ürün:\n", df.sort_values("Adet", ascending=False).head(1))
print("\nEn çok gelir getiren kategori:\n", df.groupby("Kategori")["Ciro"].sum())
