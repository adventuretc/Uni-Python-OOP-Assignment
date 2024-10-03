#  from abc import abstractmethod
from abc import ABC


class Auto(ABC):

	#  tipus: str
	#  rendszam: str
	#  berleti_dij: float
	
	#  @abstractmethod
	# mi volt a hibám: Nem szükséges abstract-ként megjelölni ezt a method-ot mivel nem úgy használom a származtatott osztályokban és amúgy is egy konstruktornak nem sok értelme van, hogy abstract legyen hiszen majdnem minden osztálynak van konstruktora.
	def __init__(self,rendszarm,tipus,berleti_dij):
		self.rendszam  = rendszarm
		self.tipus = tipus
		self.berleti_dij = berleti_dij
	