class Raza:
    def __init__(self, nosaukums, daudzums, aVAId):         #defineju ražu kā raza. (self, augļa vai dārzeņa nosaukums,tā daudzums Kg, Auglis vai dārzenis)   
        self.name = nosaukums
        self.weight = daudzums
        self.fruitorvegetable = aVAId
    def jaunais_nosaukums(self, jauns_nosaukums):
        self.name = jauns_nosaukums
    def jaunais_avaid(self, jauns_aVAId):
        self.fruitorvegetable = jauns_aVAId
    def aped(self, cik_aped):
        if cik_aped <= 0:
            raise ValueError("jābūt pozitīvam skaitlim")
        if self.weight < cik_aped:
            raise ValueError("nevari tik daudz apēst")
        self.weight -= cik_aped
    def info(self):
        return "Novākto sauc {}, tas ir {} Kg daudz un tas ir {}".format(self.name, self.weight, self.fruitorvegetable)
class Abols(Raza):
    def __init__(self, daudzums, skirne):
        super().__init__("ābols", daudzums, "aulgis")
        self.abola_skirne = skirne
    def info(self):
        abola_info = super().info()
        return f"{abola_info} ābola šķirne ir {self.abola_skirne}"



novaktais1 = Raza("abols", 1, "auglis")

print(novaktais1.info())