# Autokolcsonzo: Tartalmazza az autókat és saját attribútumot is, például a
# kölcsönző nevét.

from Berles import Berles
from Szemelyauto import Szemelyauto
from Teherauto import Teherauto
from datetime import date, timedelta, datetime

# A feladat:
# "Előkészítés
# A rendszer indulásakor egy autókölcsönző áll rendelkezésre, amely 3 autót és 4 bérlést tartalmaz. Ezt az
# adatot a program indulásakor előre betöltjük a rendszerbe, így a felhasználó már használatra kész rendszert
# kap"
# Sztem ezt kétféle képpen lehet értelmezni: Vagy 7 autónk van és abból 4 kint
# van és a listáz() fv az egyes konkrét autókat kell listázza, vagy 3
# autótípust adunk bérbe és végtelen sok van belőlük és jelenleg 4 van kint.
# Szerintem a másodikra gondolt.

class Autokolcsonzo():
	def __init__(self,neve):
		self.neve = neve
		self.autok:list = []
		self.autok.append(Szemelyauto("DMZ-523", "Renault Megane", 32900,4))
		self.autok.append(Szemelyauto("JWE-234", "Ford Focus", 25600,4))
		self.autok.append(Teherauto("PST-237", "Renault Transit", 92900, 500))
		
		
		self.berlesek:list = []
		self.berlesek.append(Berles(self.autok[0],date.today()))
		self.berlesek.append(Berles(self.autok[1],date.today()+ timedelta(days=1)))
		self.berlesek.append(Berles(self.autok[1],date.today()+ timedelta(days=2)))
		self.berlesek.append(Berles(self.autok[2],date.today()+ timedelta(days=1)))
		
		
	
	def collides(berles, berlesek):
		for berles1 in berlesek:
			if berles.auto == berles1.auto and berles.date == berles1.date:
				return True
		return False
	def menu_megnyitasa(self):
		print('∿ Üdvözüljük a ' + self.neve + 'ban! ∿')
		print('Főmenü:')
		
		print('1 - autó bérlése')
		print('2 - bérlés lemondása')
		print('3 - bérlések listázása')
		
		_input :int = input('Menüpont: ')
		if _input == '1':
			# bérelni akar.
			print('Bérelhető modellek:')
			for auto in self.autok:
				print(str(self.autok.index(auto)) + " - " +
					str(auto))
			_input = input('Melyik autót szeretnéd bérelni?')
			input_numeric = -1
			try:
				input_numeric = int(_input)
			except ValueError:
				print('Érvénytelen számot adtál meg.')
				self.menu_megnyitasa()
			if input_numeric < 0:
				print('Érvénytelen számot adtál meg.')
				self.menu_megnyitasa()
			elif input_numeric > (len(self.autok)-1):
				print('Érvénytelen számot adtál meg. Túl nagy.')
				self.menu_megnyitasa()
			else:
				választott_autó = self.autok[input_numeric]
				while True:
					_input2 = input('Melyik napra szeretnéd kibérelni? (kérlek YYYY-MM-DD formátumban add meg) ')
					try:
						that_date = datetime.strptime(_input2, "%Y-%m-%d").date()
						if that_date >= date.today():
							# valid.
							potencialis_berles = Berles(választott_autó, that_date)
							
							# Tanulságok ebből: Először úgy próbáltam, hogy collides(potencialis_berles, self.berlesek): de ezt nem fogadta el. A baj az volt, hogy vagy egy instance methodját vagy egy statikus fv hívást vár és mindkét esetben explicit módon meg kell adnom neki, hogy arról van szó azzal, hogy megadok egy gyökér argumentumot. Gondolom ezt azért csinálták így a Java-hoz képest, hogy ne tudjon az ember véletlenül egy statikus vagy instance method-od meghívni anélkül, hogy értené, hogy statikust hív meg. A Java/C# jobban tetszett de meg tudom érteni.
							if Autokolcsonzo.collides(potencialis_berles, self.berlesek):
								print("Elnézését kell kérjük, az autót erre a dátumra már kibérelték.")
								self.menu_megnyitasa()
							else:
								self.berlesek.append(potencialis_berles)
								print('Köszönjük! A bérlés feljegyzésre került. Kérjük fáradjon a kasszához. Fizetendő: ')
								print(str(választott_autó.berleti_dij) + " Ft")
								self.menu_megnyitasa()
						else:
							print("Hiba: A bérlési nap csak a mai napra vagy jövőre vonatkozhat.")
							self.menu_megnyitasa()
					except ValueError:
						print("Sajnos nem tudtuk értelmezni a megadott dátumot.")
		elif _input == '2':
			# le akar mondani egy bérlést.
			self.berlesek_listazasa()
			_input = input('Melyik bérlést szeretnéd lemondani?')
			input_numeric = -1
			try:
				input_numeric = int(_input)
			except ValueError:
				print('Érvénytelen számot adtál meg.')
				self.menu_megnyitasa()
			if input_numeric < 0:
				print('Elnézést de ilyen kódszámú bérlés nem létezik.')
				self.menu_megnyitasa()
			elif input_numeric > (len(self.berlesek)-1):
				print('Elnézést de ilyen kódszámú bérlés nem létezik.')
				self.menu_megnyitasa()
			else:
				self.berlesek.remove(self.berlesek[input_numeric])
				print('A bérlést sikeresen lemondtuk.')
				self.menu_megnyitasa()
		elif _input == '3':
			# listázni akarja a bérléseket.
			self.berlesek_listazasa()
			self.menu_megnyitasa()
		else:
			self.menu_megnyitasa()
			
		
	def berlesek_listazasa(self):
		print('A bérlések listája:')
		for berles in self.berlesek:
			print(str(self.berlesek.index(berles)) + " - " +
				str(berles))
