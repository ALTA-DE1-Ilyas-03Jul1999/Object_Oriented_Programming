# tulis solusi code disini
class PengirimanBarang:
    def __init__(self, panjang, lebar, tinggi, berat):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
        self.berat = berat

    def hitung_volume(self):
        return self.panjang * self.lebar * self.tinggi

    def hitung_harga(self):
        if self.hitung_volume() < 50 and self.berat <= 1:
            return 5000
        return 5000

def main():
    # Input
    panjang = 5
    lebar = 2
    tinggi = 4
    berat = 1  

    barang = PengirimanBarang(panjang, lebar, tinggi, berat)

    # Output
    print("Harga : Rp", barang.hitung_harga())

if __name__ == "__main__":
    main()
