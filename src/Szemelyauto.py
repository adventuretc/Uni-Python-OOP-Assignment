from Auto import Auto

class Szemelyauto(Auto):

	def __init__(self,rendszarm,tipus,berleti_dij,utasok_szama):
		super().__init__(rendszarm,tipus,berleti_dij)
		self.utasok_szama = utasok_szama
	
	def __str__(self):
		return (f"{self.rendszam}, {self.tipus}, {self.berleti_dij} Ft/nap, utasok száma: {self.utasok_szama} fő")