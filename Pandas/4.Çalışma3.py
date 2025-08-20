import pandas as pd

df = pd.read_csv(r"C:\Users\Mert\OneDrive\Masaüstü\Web Scraping\Pandas\calisanlar.csv")

print("Eksik veriler:\n", df.isnull().sum())

# Maaş sütununu sayısala çevir (hatalı değerleri NaN yapar)
df["Maaş"] = pd.to_numeric(df["Maaş"], errors="coerce")

# Eksik maaşları ortalama ile doldur
ortalama_maas = df["Maaş"].mean(skipna=True)
df["Maaş"].fillna(ortalama_maas, inplace=True)

# Eksik yaşı olan satırları sil
df.dropna(subset=["Yaş"], inplace=True)

print("\nTemizlenmiş tablo:\n", df)
