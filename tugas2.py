# Class Dosen

class Dosen :
  def __init__(self, nama, NIM, prodi, fakultas, kampus, alamat):
    self.nama = nama
    self.NIM = NIM
    self.prodi = prodi
    self.fakultas = fakultas
    self.kampus = kampus
    self.alamat = alamat

  def tampilkanProfilDosen(self):
    print("Nama", self.nama)
    print("NIM", self.NIM)
    print("Prodi", self.prodi)
    print("Fakultas", self.fakultas)
    print("Kampus", self.kampus)
    print("alamat", self.alamat)

  def cekProdi(self):
    prodi = self.prodi
    match prodi:
      case "TI":
        print("Teknik Informatika")
      case "SI":
        print("Sistem Informasi")
      case "TIF":
        print("Teknologi Informasi")
  
Dosen1 = Dosen("Adam Haris", "2565114013", "TI", "Teknologi Informasi","UNHASY","MADURA")
Dosen1.cekProdi()
Dosen1.tampilkanProfilDosen()
print()

Dosen2 = Dosen("Rocky Gerung", "2595448844", "SI", "Teknik Dilantik","GAGAL","TIKUS")
Dosen2.cekProdi()
Dosen2.tampilkanProfilDosen()
print()

Dosen3 = Dosen("ABU Ghufron", "2589887788", "TIF", "Teknik Manipulasi","GONDRONG","GENDENG")
Dosen3.cekProdi()
Dosen3.tampilkanProfilDosen()
print()