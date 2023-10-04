# tulis solusi code disini
# Definisikan kelas Kalkulator
class Kalkulator:

    @staticmethod
    def tambah(a, b):
        return a + b

    @staticmethod
    def kurang(a, b):
        return a - b

    @staticmethod
    def kali(a, b):
        return a * b

    @staticmethod
    def bagi(a, b):
        if b == 0:
            return "Error: Pembagi tidak boleh nol!"
        return a / b

# Fungsi utama
def main():
    # Input
    a1, b1 = 3, 4
    a2, b2 = 15, 4
    a3, b3 = 10, 10
    a4, b4 = 12, 3

    # Output
    print("Penjumlahan:", Kalkulator.tambah(a1, b1))
    print("Pengurangan:", Kalkulator.kurang(a2, b2))
    print("Perkalian:", Kalkulator.kali(a3, b3))
    print("Pembagian:", Kalkulator.bagi(a4, b4))

# Jalankan fungsi utama
if __name__ == "__main__":
    main()
