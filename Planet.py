import random

class Planet(object):
	def __init__(self, planetId):
		self.planetDistance = random.randint(1,300)
		self.planetId = planetId
		self.intelligent=False

	#setter Methods
	def setIntelligence(self, intelligent):
		self.intelligent = intelligent

	#Getter Methods
	def getDistance(self):
		return self.planetDistance 
	def getPlanetID(self):
		return self.planetId
	def getIntelligence(self):
		return self.intelligent


#SubClasses
class RockyPlanet(Planet):
	def __init__(self):
		Planet.__init__(self,"r")

class GaseousPlanet(Planet):
	def __init__(self):
		Planet.__init__(self,"g")

class HabitablePlanet(Planet):
	def __init__(self):
		Planet.__init__(self,"h")

