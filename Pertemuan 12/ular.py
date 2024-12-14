from Animal import *

class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, corak, racun):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.corak = corak
        self.racun = racun

    def cetak_Ular(self):
        super().cetak()
        print("design \t\t\t\t:", self.corak,
        "\nracun \t\t\t\t:", self.racun)

anaconda = Ular("anaconda", "kambing", "Amazon", "bertelur", "polkadot", "tidak berbisa")
anaconda.cetak_Ular()

cobra = Ular("cobra", "tikus", "hutan", "bertelur", "coklat kehitaman", "ssangat berbisa")
cobra.cetak_Ular()

print (" ")
    