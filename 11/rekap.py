import csv

data = []

with open("nilai.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for baris in reader:
        baris["nilai"] = int(baris["nilai"])
        data.append(baris)

rekap = {}

for d in data:
    kelas = d["kelas"]
    rekap.setdefault(kelas, []).append(d["nilai"])

print(f"{'Kelas':<6}{'Jumlah':>8}{'Rata':>8}")

for kelas, nilai in sorted(rekap.items()):
    rata = sum(nilai) / len(nilai)
    print(f"{kelas:<6}{len(nilai):>8}{rata:>8.1f}")
