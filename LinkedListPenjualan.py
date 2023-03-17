class Barang:
    def __init__(self, nama_barang, harga, stok, kode):
        self.nama_barang = nama_barang
        self.harga = harga
        self.stok = stok
        self.kode = kode
        self.next = None

    def display(self):
        print("Kode Barang : ", self.kode)
        print("Nama Barang : ", self.nama_barang)
        print("Harga : ", self.harga)
        print("Stok : ", self.stok)
        print("----------------------------")

class Penjualan:
    def __init__(self):
        self.head = None
        self.tail = None
        self.history = []

    def tambah_barang(self):
        while True:
            nama_barang = input("Masukkan nama barang (selesai untuk keluar): ")
            if nama_barang == "selesai":
                break
            harga = int(input("Masukkan harga barang: "))
            stok = int(input("Masukkan stok barang: "))
            kode = input("Masukkan kode barang: ")
            new_barang = Barang(nama_barang, harga, stok, kode)
            if self.head is None:
                self.head = new_barang
                self.tail = new_barang
            else:
                self.tail.next = new_barang
                self.tail = new_barang

            self.history.append(f"Tambah barang - {nama_barang}, kode: {kode}")

    def hapus_barang(self):
        while True:
            hapus_tambah = input("Hapus atau tambahkan barang? (h/t/selesai) ")
            if hapus_tambah == "h":
                kode = input("Masukkan kode barang yang akan dihapus (selesai untuk keluar): ")
                if kode == "selesai":
                    break
                temp = self.head
                prev = None
                while temp is not None:
                    if temp.kode == kode:
                        if prev is None:
                            self.head = temp.next
                        else:
                            prev.next = temp.next
                        del temp
                        print(f"Barang dengan kode {kode} berhasil dihapus.")
                        self.history.append(f"Hapus barang - kode: {kode}")
                        self.tampilkan_barang() # menampilkan kembali daftar barang setelah barang dihapus
                        break # keluar dari loop setelah barang dihapus
                    prev = temp
                    temp = temp.next
                else: # barang tidak ditemukan
                    print(f"Barang dengan kode {kode} tidak ditemukan.")
            elif hapus_tambah == "t":
                self.tambah_barang()
                self.tampilkan_barang()
            elif hapus_tambah == "selesai":
                return
            else:
                print("Masukan tidak valid. Silakan masukkan 'h', 't', atau 'selesai'.")

    def tampilkan_barang(self):
        temp = self.head
        while temp is not None:
            temp.display()
            temp = temp.next

    def beli_barang(self):
       kode = input("Masukkan kode barang yang akan dibeli: ")
       jumlah = int(input("Masukkan jumlah barang yang akan dibeli: "))
       temp = self.head
       while temp is not None:
        if temp.kode == kode:
            if temp.stok < jumlah:
                print("Maaf, stok barang tidak mencukupi.")
                return
            else:
                total_harga = jumlah * temp.harga
                print(f"Total harga: Rp{total_harga}")
                temp.stok -= jumlah
                self.history.append(f"Beli barang - {temp.nama_barang}, kode: {kode}")
                lanjut_belanja = input("Apakah ingin melanjutkan belanja? (l/t) ")
                if lanjut_belanja == "l":
                    self.tampilkan_barang()
                    self.beli_barang()
                elif lanjut_belanja == "t":
                    return
                else:
                    print("Masukan tidak valid. Silakan masukkan 'l' atau 't'.")
                return
            temp = temp.next
        print(f"Barang dengan kode {kode} tidak ditemukan.")
        return

penjualan = Penjualan()

# Menambahkan barang
penjualan.tambah_barang()

# Menampilkan daftar barang
print("Daftar Barang:")
penjualan.tampilkan_barang()

# Membeli barang
penjualan.beli_barang()

# Menghapus barang
penjualan.hapus_barang()

# Menampilkan history
print("History:")
for h in penjualan.history:
    print(h)