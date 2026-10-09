buah = ["apel", "jeruk", "mangga"]

print(buah)
print(buah[0])

buah.append("pisang")
buah[1] = "anggur"

print("Setelah diubah:", buah)
print("Jumlah buah:", len(buah))

for item in buah:
    print(item)
