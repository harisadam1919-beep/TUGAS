"""Analisis nilai mahasiswa menggunakan list comprehension, lambda, filter, dan sorted."""

data_mahasiswa = [
    {"nama": "Aisyah", "nim": "230101", "tugas": 85, "uts": 80, "uas": 88},
    {"nama": "Budi", "nim": "230102", "tugas": 70, "uts": 65, "uas": 75},
    {"nama": "Cantika", "nim": "230103", "tugas": 90, "uts": 85, "uas": 92},
    {"nama": "Dimas", "nim": "230104", "tugas": 78, "uts": 82, "uas": 80},
    {"nama": "Eka", "nim": "230105", "tugas": 88, "uts": 91, "uas": 86},
]

# List comprehension untuk membuat data baru dengan nilai akhir.
hasil = [
    {
        **mhs,
        "nilai_akhir": round(mhs["tugas"] * 0.30 + mhs["uts"] * 0.30 + mhs["uas"] * 0.40, 2),
    }
    for mhs in data_mahasiswa
]

berprestasi = list(filter(lambda mhs: mhs["nilai_akhir"] > 80, hasil))
ranking = sorted(hasil, key=lambda mhs: mhs["nilai_akhir"], reverse=True)

print("=" * 58)
print("              ANALISIS NILAI MAHASISWA")
print("=" * 58)
print("Bobot: Tugas 30% | UTS 30% | UAS 40%")
print("\nDAFTAR RANKING")
for posisi, mhs in enumerate(ranking, start=1):
    print(f"{posisi}. {mhs['nama']:<10} NIM: {mhs['nim']} | "
          f"Tugas: {mhs['tugas']:>3} | UTS: {mhs['uts']:>3} | "
          f"UAS: {mhs['uas']:>3} | Akhir: {mhs['nilai_akhir']:>5.2f}")

print("\nMAHASISWA BERP​​RESTASI (nilai akhir > 80)".replace("\u200b", ""))
for mhs in berprestasi:
    print(f"- {mhs['nama']}: {mhs['nilai_akhir']:.2f}")

terbaik = ranking[0]
print("\nMAHASISWA TERBAIK")
print(f"Nama: {terbaik['nama']} | NIM: {terbaik['nim']} | Nilai akhir: {terbaik['nilai_akhir']:.2f}")
