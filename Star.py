import random
from Planet import * 

class Star(object):
	def __init__(self,typeOfStar, chancesOfLife, numberOfPlanets, galdilocksZone, reChargeAmount):
		self.chancesOfLife = chancesOfLife
		self.numberOfPlanets = numberOfPlanets
		self.galdilocksZone = galdilocksZone
		self.reChargeAmount = reChargeAmount
		self.x=0
		self.y=0
		self.z=0
		self.typeOfStar=typeOfStar
		self.planets = []
		self.isVisited=False 

	def chancesOfLifeHelper(self):
		tmp = random.randint(0,1000)
		if(tmp < self.chancesOfLife * 100000):
			return True
		return False

	def generatePlanet(self):
		numOfRocky = 0
		numOfGaseous = 0
		numOfHabitable = 0
		numOfLife = 0
		for index, i in enumerate(self.planets):
			self.chancesOfLifeHelper()

			if(i.getPlanetID() == 'h' and i.getDistance() <= self.galdilocksZone and self.chancesOfLifeHelper()):
				numOfLife = numOfLife + 1
				self.planets[index].setIntelligence(True)
			if(i.getPlanetID() == 'g'):
				numOfGaseous = numOfGaseous + 1
			elif(i.getPlanetID() == 'r'):
				numOfRocky = numOfRocky + 1
			else:
				numOfHabitable = numOfHabitable + 1
		
		return [numOfRocky, numOfGaseous, numOfHabitable, numOfLife]

	def setCoordinate(self):
		self.x = random.randint(2**3,2**64-1)
		self.y=random.randint(2**3,2**64-1)
		self.z=random.randint(2**3,2**64-1)

	def getCoordinate(self):
		return [self.x, self.y, self.z]
	def getPlanets(self):
		return self.planets
	def getReChargeAmount(self):
		return self.reChargeAmount
	def getChancesOfLife(self):
		return self.chancesOfLife

	#Setter methods
	def setVisited(self):
		self.isVisited = True
	#Getter methods
	def getType(self):
		return self.typeOfStar
	def getVisited(self):
		return self.isVisited

class DwarfStar(Star):
	def __init__(self):
		Star.__init__(self,"d",0.0006,random.randint(8,15),random.randint(30,90),2**20)

		for i in range(self.numberOfPlanets):
			typeOfPlanet = random.randint(1,3)
			if(typeOfPlanet == 1):
				tmpPlanet = RockyPlanet()
				self.planets.append(tmpPlanet)
			elif(typeOfPlanet == 2):
				tmpPlanet = GaseousPlanet()
				self.planets.append(tmpPlanet)
			else:
				tmpPlanet = HabitablePlanet()
				self.planets.append(tmpPlanet)

class GiantStar(Star):
	def __init__(self):
		Star.__init__(self,"g",0.0005,random.randint(5,10),random.randint(100,250),2**30)

		for i in range(self.numberOfPlanets):
			typeOfPlanet = random.randint(1,3)
			if(typeOfPlanet == 1):
				tmpPlanet = RockyPlanet()
				self.planets.append(tmpPlanet)
			elif(typeOfPlanet == 2):
				tmpPlanet = GaseousPlanet()
				self.planets.append(tmpPlanet)
			else:
				tmpPlanet = HabitablePlanet()
				self.planets.append(tmpPlanet)


class MediumStar(Star):
	def __init__(self):
		Star.__init__(self,"m",0.0009,random.randint(5,10),random.randint(60,140),2**30)
	
		for i in range(self.numberOfPlanets):
			typeOfPlanet = random.randint(1,3)
			if(typeOfPlanet == 1):
				tmpPlanet = RockyPlanet()
				self.planets.append(tmpPlanet)
			elif(typeOfPlanet == 2):
				tmpPlanet = GaseousPlanet()
				self.planets.append(tmpPlanet)
			else:
				tmpPlanet = HabitablePlanet()
				self.planets.append(tmpPlanet)

