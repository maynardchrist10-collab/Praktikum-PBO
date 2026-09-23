# class MesinATM:
#     def __init__(self, id_atm, lokasi, saldo_kas):
#         self.id_atm = id_atm
#         self.lokasi = lokasi
#         self.saldo_kas = saldo_kas

#     def proses_penarikan(self, nama_nasabah, jumlah):
#             if jumlah <= self.saldo_kas:
#                 self.saldo_kas -= jumlah
#             print(f" [ATM {self.id_atm}] Penarikan Rp{jumlah:,} oleh
# {nama_nasabah} berhasil.")

# print(f" Sisa kas di ATM {self.lokasi}: Rp{self.saldo_kas:,}")
#             else:
#                 print(f" [ATM {self.id_atm}] Saldo kas mesin tidak

# mencukupi.")
# class Nasabah:
# def __init__(self, nama, nomor_rekening):
# self.nama = nama
# self.nomor_rekening = nomor_rekening
# # Tidak ada self.atm = ...
# # Nasabah tidak memiliki mesin ATM secara permanen.
# def tarik_tunai(self, atm, jumlah):
# """Asosiasi: MesinATM diterima sebagai parameter dan dipakai
# sementara."""
# print(f" {self.nama} memasukkan kartu ke ATM unit {atm.id_atm}
# ({atm.lokasi})...")
# atm.proses_penarikan(self.nama, jumlah)
# # Kedua objek dibuat secara independen
# atm_pusat = MesinATM("ATM-01", "Kantor Cabang Sudirman", 50000000)
# budi = Nasabah("Budi Santoso", "101-220-334")
# siti = Nasabah("Siti Rahma", "101-445-889")
# # Asosiasi berjalan saat method dipanggil
# budi.tarik_tunai(atm_pusat, 500000)
# # Mesin ATM yang sama bisa digunakan oleh nasabah lain
# siti.tarik_tunai(atm_pusat, 1000000)

class Hero:
    def__init__
