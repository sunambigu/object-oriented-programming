class Mahasiswa:
    def __init__(self, nim, nama, nilaiTugas, nilaiUTS, nilaiUAS):
        self.nim = nim
        self.nama = nama
        self.nilaiTugas = nilaiTugas
        self.nilaiUTS = nilaiUTS
        self.nilaiUAS = nilaiUAS

    def hitungNilaiAKhir(self):
        nilaiAkhir = 0.2 * self.nilaiTugas + 0.3 * self.nilaiUTS + 0.5 * self.nilaiUAS

        return nilaiAkhir

daftarMahasiswa = []
print("Menu")
print("1. Input Data")
print("2. Tampilkan Data")
print("3. Keluar")

while True:
    pilihan = int(input("Masukan pilihan anda:"))


    if pilihan == 1:
        nim = input("Masukan NIM:")
        nama = input("Masukan Nama:")
        tugas = float(input("Masukan Nilai Tugas:")) #input dan casting ke float
        uts = float(input("Masukan Nilai UTS:")) #input dan casting ke float
        uas = float(input("Masukan Nilai UAS:")) #input dan casting ke float

        newMahasiswa = Mahasiswa(nim, nama, tugas, uts, uas)
        daftarMahasiswa.append(newMahasiswa)

    elif pilihan == 2:
        for mahasiswa in daftarMahasiswa:
            print(f"NIM: {mahasiswa.nim} Nama: {mahasiswa.nama} Nilai Akhir: {mahasiswa.hitungNilaiAKhir():.2f}")

    elif pilihan == 3:
        break