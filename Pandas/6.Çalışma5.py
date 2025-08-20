import pandas as pd

df = pd.read_csv(r"C:\Users\Mert\OneDrive\Masaüstü\Web Scraping\Pandas\siparisler.csv")

print("Sütunlar:", df.columns)
print(df.head())

df.columns = df.columns.str.strip()

if "Tarih" in df.columns:
    tarih_sutun = "Tarih"
elif "tarih" in df.columns:
    tarih_sutun = "tarih"
elif "Sipariş Tarihi" in df.columns:
    tarih_sutun = "Sipariş Tarihi"
else:
    raise KeyError("CSV dosyanda 'Tarih' sütunu bulunamadı, sütun adlarını kontrol et!")

df[tarih_sutun] = pd.to_datetime(df[tarih_sutun])

print("\nAylara göre sipariş sayısı:\n", df[tarih_sutun].dt.month.value_counts())

print("\nEn çok sipariş verilen gün:", df[tarih_sutun].dt.day.value_counts().idxmax())
