import matplotlib.pyplot as plt

# Veri Setleri
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
kategori = ['A', 'B', 'C']
degerler = [10, 15, 7]
dagilim = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]

# Grafik Alanı (2 satır, 3 sütun)
plt.figure(figsize=(12, 8))

# 1. Çizgi Grafiği
plt.subplot(2, 3, 1)
plt.plot(x, y, color='blue', linestyle='--', marker='o')
plt.title("Çizgi Grafiği")
plt.xlabel("X Ekseni")
plt.ylabel("Y Ekseni")
plt.grid(True)

# 2. Çubuk Grafiği
plt.subplot(2, 3, 2)
plt.bar(kategori, degerler, color='green')
plt.title("Çubuk Grafiği")
plt.xlabel("Kategori")
plt.ylabel("Değer")

# 3. Dağılım Grafiği
plt.subplot(2, 3, 3)
plt.scatter(x, y, color='red', marker='s')
plt.title("Dağılım Grafiği")
plt.xlabel("X Ekseni")
plt.ylabel("Y Ekseni")

# 4. Histogram
plt.subplot(2, 3, 4)
plt.hist(dagilim, bins=5, color='orange', alpha=0.7)
plt.title("Histogram")
plt.xlabel("Değerler")
plt.ylabel("Frekans")

# 5. Pasta Grafiği
plt.subplot(2, 3, 5)
plt.pie(degerler, labels=kategori, autopct="%1.1f%%", colors=['purple', 'cyan', 'pink'])
plt.title("Pasta Grafiği")

# 6. Kombinasyon Grafiği
plt.subplot(2, 3, 6)
plt.plot(x, y, label='Çizgi', color='blue')
plt.scatter(x, y, label='Noktalar', color='red')
plt.bar(kategori, degerler, label='Çubuk', color='green', alpha=0.5)
plt.title("Kombine Grafik")
plt.legend()

# Genel Başlık ve Düzenleme
plt.suptitle("Matplotlib Genel Çalışma - Tüm Grafik Türleri", fontsize=14)
plt.tight_layout()
plt.savefig("tum_grafikler.png")
plt.show()
