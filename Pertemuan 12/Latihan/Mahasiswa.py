from Person import *
class Mahasiswa(Person):
    prodi = ""
    semester = ""
    
    def __init__(self, nama, gender, umur, prodi, semester):
        super()._init_(nama, gender, umur)
        self.prodi = prodi
        self.semester = semester 
    
    def cetak(self):
        super().cetak()
        print("Prodi \t\t\t:", self.prodi,
              "\nSemester \t\t:", self.semester,
              "\n-------------------------------")