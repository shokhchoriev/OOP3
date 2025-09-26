class Maktab:
    def __init__(self,nomi,manzil,oquvchilar_soni,direktor):
        self.nom = nomi
        self.manzil = manzil
        self.oquvchilar_soni = oquvchilar_soni
        self.direktor = direktor
    def info(self):
         return f"{self.manzil} da {self.nom} maktabda {self.oquvchilar_soni} oquvchi bor direktori {self.direktor}"

maktab1 = Maktab("21-maktab", "toshkent", 122 , "Ali")
maktab2 = Maktab("12-maktab", "fargona", 9 , "vali")
maktab3 = Maktab("30-maktab", "andijon", 143 , "eshmat")

print(maktab1.info())



class Student:
    def __init__(self,ism,manzil,baho,yosh):
        self.ism = ism
        self.manzil = manzil
        self.baho = baho
        self.yosh = yosh
    def get_manzil(self):
        return f"{self.ism} {self.manzil}lik"
    def info(self):
        return f"{self.ism} {self.manzil}da {self.baho} ga oqiydi.U {self.yosh}"
    
bola1 = Student("Aziz", "bogdod",5,18)
bola2 = Student("Shaxlo", "russia",4,18)

print(bola1.get_manzil())


    