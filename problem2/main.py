# tulis solusi code disini
class BangunRuang:
    def volume(self):
        pass
    
class Kubus(BangunRuang):
    def __init__ (self, sisi):
        self.sisi = sisi
    def volume (self):
        return self.sisi ** 3
    
class Balok(BangunRuang):
    def __init__ (self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
    def volume (self):
        return self.panjang * self.lebar * self.tinggi

class Tabung(BangunRuang):
    def __init__ (self, jari_jari, tinggi):
        self.jari_jari = jari_jari
        self.tinggi = tinggi
    def volume(self):
        return 3.14 * (self.jari_jari ** 2) * self.tinggi
    
def main():
    kubus = Kubus(10)
    balok = Balok(3,6,10)
    tabung = Tabung(7,10)
    
    print("Volume")
    print(f"Kubus : {kubus.volume()}")
    print(f"Balok : {balok.volume()}")
    print(f"Tabung : {tabung.volume()}")

if __name__ == "__main__":
    main()