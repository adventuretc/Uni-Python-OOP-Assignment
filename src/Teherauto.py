from Auto import Auto
# mi volt a hibám: ezt írtam:
# from beadandó_1 import Auto, és erre elhasalt és panaszkodott, hogy az Auto
# nem 3 hanem 2 positional argumentet fogad. De mit jelent ez szerinte
# szintaktikailag? És mi az a 2 argumentum?

class Teherauto(Auto):
	def __init__(self, rendszarm, tipus, berleti_dij, teherbiras_kg):
		super().__init__(rendszarm, tipus, berleti_dij)
		# mi volt a hibám: ezt írtam:
		# super.__init__(rendszarm, tipus, berleti_dij)
		# Vajon mire gondoltak amikor ezt kitalálták?
		self.teherbiras_kg = teherbiras_kg
		
	
	def __str__(self):
		return (f"{self.rendszam}, {self.tipus}, {self.berleti_dij} Ft/nap, teherbírás: {self.teherbiras_kg} kg")