class Raza:
    def __init__(self, nosaukums, daudzums, aVAId):         #defineju ražu kā raza. (self, augļa vai dārzeņa nosaukums,tā daudzums Kg, Auglis vai dārzenis)   
        self.name = nosaukums
        self.weight = daudzums
        self.fruitorvegetable = aVAId

    def info(self):
        return "Novākto sauc {}, tas ir {} Kg daudz un tas ir {}".format(self.name, self.weight, self.fruitorvegetable)

novaktais1 = Raza("abols", 1, "auglis")

print(novaktais1.info())