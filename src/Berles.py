# Berles: Az autóbérléshez szükséges osztály, amely egy autó bérlését egy
# napra tárolja.

from datetime import date
from typing import overload

from gi.overrides import override
from mercurial.thirdparty.attr.validators import instance_of
from numba.core.extending import overload_method

from Auto import Auto
from Szemelyauto import Szemelyauto
from Teherauto import Teherauto


class Berles():
	
	# jesus: nem lehet több konstruktor.
	# https://stackoverflow.com/questions/2164258/is-it-not
	# -possible-to-define-multiple-constructors-in-python
	# rádásul ha 2 konstruktort adok meg akkor a 2. hiba dobása nélkül
	# felülírja az elsőt és az első elvész.
	#  @classmethod
	#  def from_filename(cls, name):
	#  return cls(open(name, 'rb'))
	
	def __init__(self, auto:Auto, date1: date):
		self.auto: Auto = auto
		self.date: date = date1
	
	def __str__(self):
		return (f"{str(self.auto)}, bérlés napja: {self.date}")
