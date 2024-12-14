from Animal import *

class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, design, cara_berenang):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.design = design
        self.cara_berenang = cara_berenang

    def cetak_Ikan(self):
        super().cetak()
        print("design \t\t\t\t:", self.design,
        "\ncara berenang \t\t\t:", self.cara_berenang)

Badut = Ikan("Badut", "plankton", "air asin", "bertelur", "belang oren putih hitam", "lambat")
Badut.cetak_Ikan()

Marlin = Ikan("marlin", "cumi-cumi", "air asin", "bertelur", "biru hitam abu", "lambat")
Marlin.cetak_Ikan()

print(" ")