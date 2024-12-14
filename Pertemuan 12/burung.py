from Animal import *

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, design, paruh):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.design = design
        self.paruh = paruh

    def cetak_Burung(self):
        super().cetak()
        print("design \t\t\t\t:", self.design,
        "\nparuh \t\t\t\t:", self.paruh)

beo = Burung("beo", "kacang", "hutanhujan", "bertelur", "hitam", "bengkok")
beo.cetak_Burung()

pelatuk = Burung("pelatuk", "ulet", "hujan", "bertelur", "coklat", "bengkok")
pelatuk.cetak_Burung()

print("  ")
    