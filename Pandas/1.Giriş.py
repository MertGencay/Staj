import pandas as pd

# CSV dosyasını oku
df = pd.read_csv(r"C:\Users\Mert\OneDrive\Masaüstü\Web Scraping\Pandas\ogrenciler.csv")


# ------------------------------
# 1. Genel Bilgi Alma
# ------------------------------
print("İlk 5 satır:\n", df.head())
print("\nTablo boyutu (satır, sütun):", df.shape)
print("\nSütun isimleri:", df.columns)
print("\nVeri tipleri:\n", df.dtypes)
print("\nÖzet bilgiler:\n")
print(df.info())
print("\nİstatistiksel özet:\n", df.describe())

# ------------------------------
# 2. Veri Seçme
# ------------------------------
print("\nSadece 'Ad' sütunu:\n", df["Ad"])
print("\n2. satır (index=1):\n", df.loc[1])
print("\n3. öğrencinin Not'u (index=2):", df.loc[2, "Not"])

# ------------------------------
# 3. Veri İşleme
# ------------------------------
print("\nNotlara göre sıralama:\n", df.sort_values("Not"))
print("\nSütun adlarını değiştirme (Not -> Puan):\n", df.rename(columns={"Not": "Puan"}))
print("\nSadece 'Ad' ve 'Yaş' sütunlarını seç:\n", df[["Ad", "Yaş"]])

# ------------------------------
# 4. Veri Analizi
# ------------------------------
print("\nŞehirlerdeki öğrenci sayısı:\n", df["Şehir"].value_counts())
print("\nYaş ortalaması:", df["Yaş"].mean())
print("\nNotların en küçüğü:", df["Not"].min())
print("Notların en büyüğü:", df["Not"].max())

# Gruplama örneği
print("\nŞehirlere göre ortalama notlar:\n", df.groupby("Şehir")["Not"].mean())

# ------------------------------
# 5. Dosya İşlemleri
# ------------------------------
# df.to_csv("ogrenciler_yeni.csv", index=False)
# print("\nYeni CSV dosyası kaydedildi: ogrenciler_yeni.csv")
