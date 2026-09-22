# """
# Sistem Manajemen Presensi Karyawan
# ==================================
# Tugas Pemrograman Berorientasi Objek (PBO)
# Menerapkan materi dari:
#   - Modul 1: Pengantar OOP, Class, dan Object
#   - Modul 2: Atribut dan Method
#   - Modul 3: Encapsulation dan Property
# """


class Karyawan:
    """Merepresentasikan data seorang karyawan."""

    # ----- Atribut Kelas (dipakai bersama oleh seluruh objek Karyawan) -----
    nama_perusahaan = "PT Maju Bersama Sejahtera"
    jam_masuk_standar = "08:00"
    total_karyawan = 0

    def __init__(self, nama, id_karyawan, jabatan, gaji_pokok):
        # Atribut instance - Public
        self.nama = nama
        self.id_karyawan = id_karyawan
        self.jabatan = jabatan
        # Atribut instance - Private (data sensitif)
        self.__gaji_pokok = gaji_pokok

        Karyawan.total_karyawan += 1

    # ----- Property: Getter & Setter untuk gaji_pokok (private) -----
    @property
    def gaji_pokok(self):
        """Getter -- mengambil nilai gaji pokok."""
        return self.__gaji_pokok

    @gaji_pokok.setter
    def gaji_pokok(self, nilai_baru):
        """Setter -- memvalidasi gaji pokok sebelum diubah."""
        if nilai_baru <= 0:
            print(f"[Ditolak] Gaji pokok {self.nama} harus lebih besar dari 0.")
        else:
            self.__gaji_pokok = nilai_baru
            print(f"Gaji pokok {self.nama} berhasil diperbarui menjadi Rp{nilai_baru:,}")

    # ----- Instance Method -----
    def tampilkan_info(self):
        """Menampilkan informasi lengkap karyawan."""
        print(f"ID         : {self.id_karyawan}")
        print(f"Nama       : {self.nama}")
        print(f"Jabatan    : {self.jabatan}")
        print(f"Gaji Pokok : Rp{self.__gaji_pokok:,}")
        print(f"Perusahaan : {Karyawan.nama_perusahaan}")

    # ----- Class Method -----
    @classmethod
    def dari_dict(cls, data):
        """Factory method: membuat objek Karyawan dari dictionary."""
        return cls(data["nama"], data["id_karyawan"], data["jabatan"], data["gaji_pokok"])

    @classmethod
    def ubah_jam_masuk_standar(cls, jam_baru):
        """Mengubah jam masuk standar untuk seluruh karyawan sekaligus."""
        cls.jam_masuk_standar = jam_baru

    # ----- Static Method -----
    @staticmethod
    def validasi_id_karyawan(id_karyawan):
        """Memvalidasi format ID karyawan: harus diawali 'EMP' + 3 digit angka."""
        return (
            len(id_karyawan) == 6
            and id_karyawan.startswith("EMP")
            and id_karyawan[3:].isdigit()
        )


class Presensi:
    """Merepresentasikan satu catatan kehadiran seorang karyawan pada tanggal tertentu."""

    # ----- Atribut Kelas -----
    status_tepat_waktu = "Tepat Waktu"
    status_terlambat = "Terlambat"
    total_presensi_tercatat = 0

    def __init__(self, karyawan, tanggal, jam_masuk):
        # Atribut instance - Public
        self.karyawan = karyawan  # objek Karyawan (class saling berinteraksi)
        self.tanggal = tanggal
        # Atribut instance - Private
        self.__jam_masuk = None
        self.jam_masuk = jam_masuk  # diisi lewat setter agar tervalidasi
        self.__status = None

        Presensi.total_presensi_tercatat += 1

    # ----- Property: Getter & Setter untuk jam_masuk (private) -----
    @property
    def jam_masuk(self):
        """Getter -- mengambil jam masuk."""
        return self.__jam_masuk

    @jam_masuk.setter
    def jam_masuk(self, waktu_baru):
        """Setter -- memvalidasi format jam masuk (HH:MM, 00-23 : 00-59)."""
        bagian = waktu_baru.split(":")
        valid = (
            len(bagian) == 2
            and bagian[0].isdigit()
            and bagian[1].isdigit()
            and 0 <= int(bagian[0]) <= 23
            and 0 <= int(bagian[1]) <= 59
        )
        if not valid:
            print(f"[Ditolak] Format jam masuk '{waktu_baru}' tidak valid. Gunakan format HH:MM.")
        else:
            self.__jam_masuk = waktu_baru

    # ----- Instance Method -----
    def catat_status(self):
        """Menentukan status kehadiran (tepat waktu / terlambat) berdasarkan jam standar."""
        keterlambatan = Presensi.hitung_keterlambatan(self.__jam_masuk, Karyawan.jam_masuk_standar)
        self.__status = Presensi.status_terlambat if keterlambatan > 0 else Presensi.status_tepat_waktu
        return self.__status

    def tampilkan_presensi(self):
        """Menampilkan detail presensi karyawan."""
        status = self.catat_status()
        print(f"{self.tanggal} - {self.karyawan.nama} masuk jam {self.__jam_masuk} ({status})")

    # ----- Class Method -----
    @classmethod
    def dari_string(cls, karyawan, data_str):
        """Factory method: membuat objek Presensi dari string 'tanggal,jam_masuk'."""
        tanggal, jam_masuk = data_str.split(",")
        return cls(karyawan, tanggal.strip(), jam_masuk.strip())

    @classmethod
    def reset_total_presensi(cls):
        """Mereset penghitung total presensi yang tercatat."""
        cls.total_presensi_tercatat = 0

    # ----- Static Method -----
    @staticmethod
    def hitung_keterlambatan(jam_masuk, jam_standar):
        """Menghitung selisih menit antara jam masuk dan jam standar (positif = terlambat)."""
        jm_h, jm_m = map(int, jam_masuk.split(":"))
        std_h, std_m = map(int, jam_standar.split(":"))
        return (jm_h * 60 + jm_m) - (std_h * 60 + std_m)


class ManajemenPresensi:
    """Mengelola kumpulan data presensi untuk suatu departemen (berinteraksi dengan objek Presensi)."""

    # ----- Atribut Kelas -----
    nama_sistem = "SIMPEG - Sistem Presensi Karyawan"
    versi = "1.0"
    batas_toleransi_menit = 15

    def __init__(self, nama_departemen):
        # Atribut instance - Public
        self.nama_departemen = nama_departemen
        # Atribut instance - Private
        self.__daftar_presensi = []

    # ----- Property: Getter & Setter untuk daftar_presensi (private) -----
    @property
    def daftar_presensi(self):
        """Getter -- mengambil salinan daftar presensi (data asli tetap terlindungi)."""
        return list(self.__daftar_presensi)

    @daftar_presensi.setter
    def daftar_presensi(self, daftar_baru):
        """Setter -- memvalidasi bahwa data yang dimasukkan berupa list berisi objek Presensi."""
        if not isinstance(daftar_baru, list) or not all(isinstance(p, Presensi) for p in daftar_baru):
            print("[Ditolak] daftar_presensi harus berupa list yang berisi objek Presensi.")
        else:
            self.__daftar_presensi = daftar_baru
            print(f"Daftar presensi {self.nama_departemen} berhasil diperbarui.")

    # ----- Instance Method -----
    def tambah_presensi(self, presensi):
        """Menambahkan satu objek Presensi ke dalam daftar departemen ini."""
        self.__daftar_presensi.append(presensi)
        print(f"Presensi {presensi.karyawan.nama} pada {presensi.tanggal} ditambahkan ke {self.nama_departemen}.")

    def tampilkan_rekap(self):
        """Menampilkan seluruh rekap presensi pada departemen ini."""
        print(f"\n=== Rekap Presensi - {self.nama_departemen} "
              f"({ManajemenPresensi.nama_sistem} v{ManajemenPresensi.versi}) ===")
        if not self.__daftar_presensi:
            print("Belum ada data presensi.")
            return
        for p in self.__daftar_presensi:
            p.tampilkan_presensi()

    # ----- Class Method -----
    @classmethod
    def ubah_batas_toleransi(cls, menit_baru):
        """Mengubah batas toleransi keterlambatan (berlaku untuk seluruh objek)."""
        cls.batas_toleransi_menit = menit_baru

    @classmethod
    def buat_default(cls):
        """Factory method: membuat objek ManajemenPresensi dengan nama departemen default."""
        return cls("Departemen Umum")

    # ----- Static Method -----
    @staticmethod
    def validasi_nama_departemen(nama):
        """Memvalidasi bahwa nama departemen tidak kosong."""
        return isinstance(nama, str) and len(nama.strip()) > 0


# =========================================================
# MAIN PROGRAM - PENGUJIAN
# =========================================================
if __name__ == "__main__":
    print("=" * 65)
    print("DEMO SISTEM MANAJEMEN PRESENSI KARYAWAN")
    print("=" * 65)

    # ---------- 1. Class Karyawan ----------
    print("\n--- Membuat Objek Karyawan ---")
    karyawan1 = Karyawan("Budi Santoso", "EMP001", "Staff Gudang", 4500000)
    karyawan2 = Karyawan.dari_dict({
        "nama": "Siti Aminah",
        "id_karyawan": "EMP002",
        "jabatan": "Staff Admin",
        "gaji_pokok": 5000000,
    })

    karyawan1.tampilkan_info()
    print()
    karyawan2.tampilkan_info()
    print(f"\nTotal karyawan terdaftar (atribut kelas): {Karyawan.total_karyawan}")

    print("\n--- Uji Static Method: validasi_id_karyawan ---")
    print("EMP001 valid?", Karyawan.validasi_id_karyawan("EMP001"))
    print("XX123 valid? ", Karyawan.validasi_id_karyawan("XX123"))

    print("\n--- Uji Class Method: ubah_jam_masuk_standar ---")
    print("Jam masuk standar sebelum:", Karyawan.jam_masuk_standar)
    Karyawan.ubah_jam_masuk_standar("08:30")
    print("Jam masuk standar sesudah:", Karyawan.jam_masuk_standar)

    print("\n--- Uji Setter gaji_pokok (valid & tidak valid) ---")
    karyawan1.gaji_pokok = 4800000     # valid
    karyawan1.gaji_pokok = -1000000    # tidak valid -> ditolak

    # ---------- 2. Class Presensi ----------
    print("\n--- Membuat Objek Presensi ---")
    presensi1 = Presensi(karyawan1, "22-09-2026", "08:15")
    presensi2 = Presensi.dari_string(karyawan2, "22-09-2026, 08:45")

    presensi1.tampilkan_presensi()
    presensi2.tampilkan_presensi()
    print(f"\nTotal presensi tercatat (atribut kelas): {Presensi.total_presensi_tercatat}")

    print("\n--- Uji Setter jam_masuk (valid & tidak valid) ---")
    presensi1.jam_masuk = "09:00"   # valid
    presensi1.jam_masuk = "25:99"   # tidak valid -> ditolak

    print("\n--- Uji Static Method: hitung_keterlambatan ---")
    selisih = Presensi.hitung_keterlambatan("08:45", Karyawan.jam_masuk_standar)
    print(f"Selisih dari jam standar: {selisih} menit")

    # ---------- 3. Class ManajemenPresensi ----------
    print("\n--- Membuat Objek ManajemenPresensi ---")
    manajemen1 = ManajemenPresensi("Departemen Gudang")
    manajemen2 = ManajemenPresensi.buat_default()

    manajemen1.tambah_presensi(presensi1)
    manajemen1.tambah_presensi(presensi2)
    manajemen1.tampilkan_rekap()
    manajemen2.tampilkan_rekap()

    print("\n--- Uji Class Method: ubah_batas_toleransi ---")
    print("Batas toleransi sebelum:", ManajemenPresensi.batas_toleransi_menit)
    ManajemenPresensi.ubah_batas_toleransi(10)
    print("Batas toleransi sesudah:", ManajemenPresensi.batas_toleransi_menit)

    print("\n--- Uji Static Method: validasi_nama_departemen ---")
    print("'Departemen HRD' valid?", ManajemenPresensi.validasi_nama_departemen("Departemen HRD"))
    print("''              valid?", ManajemenPresensi.validasi_nama_departemen(""))

    print("\n--- Uji Setter daftar_presensi (valid & tidak valid) ---")
    manajemen2.daftar_presensi = [presensi1, presensi2]   # valid
    manajemen2.daftar_presensi = "bukan list"              # tidak valid -> ditolak