import pandas as pd

df = pd.read_csv(r"C:\Users\Mert\OneDrive\Masaüstü\Web Scraping\Pandas\sehirler.csv")

print("En kalabalık 5 şehir:\n", df.sort_values("Nufus", ascending=False).head(5))
print("\nOrtalama nüfus:", df["Nufus"].mean())

buyuk_sehirler = df[df["Nufus"] > 1000000]
print("\n1 milyon üstü şehirler:\n", buyuk_sehirler)

# Yeni CSV kaydet
buyuk_sehirler.to_csv("buyuk_sehirler.csv", index=False)
