# tulis solusi code disini

class BangunDatar:
    def luas(self):
        pass
    
    def keliling(self):
        pass
    
class Persegi(BangunDatar):
    def __init__ (self,sisi):
        self.sisi = sisi
        
    def luas(self):
        return self.sisi ** 2
    def keliling(self):
        return 4 * self.sisi
    
class Segitiga(BangunDatar):
    def __init__ (self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
        
    def luas (self):
        return 0.5 * self.alas * self.tinggi
    def keliling(self):
        rumus = (self.alas ** 2 + self.tinggi ** 2) ** 0.5
        return self.alas + self.tinggi + rumus
    
class PersegiPanjang(BangunDatar):
    def __init__ (self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
        
    def luas(self):
        return self.panjang * self.lebar
    def keliling(self):
        return 2 * (self.panjang + self.lebar)
    
def main():
    persegi = Persegi(4)
    segitiga = Segitiga(3, 4)
    persegi_panjang = PersegiPanjang(7,8)
    
    print("Luas")
    print(f"Persegi : {persegi.luas()}")
    print(f"Segitiga : {segitiga.luas()}")
    print(f"Persegi Panjang : {persegi_panjang.luas()}")

    # Output Keliling
    print("Keliling")
    print(f"Persegi : {persegi.keliling()}")
    print(f"Segitiga : {segitiga.keliling()}")
    print(f"Persegi Panjang : {persegi_panjang.keliling()}")

# Jalankan fungsi utama
if __name__ == "__main__":
    main()