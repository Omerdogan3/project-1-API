import random
from Star import * 
from Planet import * 

class Universe(object):
	def __init__(self, numberOfStars):
		self.tmpList = []
		self.numberOfStars = numberOfStars

		self.bossCoordinates = []

		self.medNumOfStars=0     
		self.giantNumOfStars=0
		self.dwarfNumOfStars=0

		for i in range(numberOfStars):
			randStar = random.randint(1,3)
			if(randStar == 1):
				star = DwarfStar()
				self.uniqueCoordinates(star)
			elif(randStar==2):
				star = GiantStar()
				self.uniqueCoordinates(star)
			elif(randStar==3):
				star = MediumStar()
				self.uniqueCoordinates(star)
		
	def printHelper(self, starPlanet):
		print("	"+str(starPlanet[0])+" Gaseous Planets")
		print("	"+str(starPlanet[1])+" Habitable Planets")
		print("	"+str(starPlanet[2])+" Rocky Planets")
		print("	"+str(starPlanet[3])+" Planets with Intelligent Life")

	def uniqueCoordinates(self,star):
		star.setCoordinate() #define a random x,y,z value
		coordinates = star.getCoordinate() 
		if(coordinates in self.bossCoordinates): #if coordinates exists
			self.uniqueCoordinates(star) #call this function again
		else: # otherwise
			self.bossCoordinates.append(coordinates) #append and return
			self.tmpList.append(star)
			return

	def getList(self):
		return self.tmpList

	def getListLength(self):
		return len(self.tmpList)

	def getCoordinates(self):
		tmpList = []
		for star in self.tmpList:
			tmpPlanet = []
			for planet in star.getPlanets():
				tmpPlanet.append({"planetType": planet.getPlanetID(), "distance": planet.getDistance(), "intelligence": planet.getIntelligence()})

			
			tmpList.append({"coordinate": star.getCoordinate(), "starType": star.getType(), "tmpPlanet": tmpPlanet})
		return tmpList

	def getStarData(self):
		return {
			"numberOfStars": self.numberOfStars,
			"dwarfNumOfStars": self.dwarfNumOfStars,
			"medNumOfStars": self.medNumOfStars,
			"giantNumOfStars": self.giantNumOfStars
		}

	def printUniverse(self):
		print("Total Number of star(s) : ",self.numberOfStars)
		
		mediumStarPlanet=[0,0,0,0]
		dwarfStarPlanet=[0,0,0,0]
		giantStarPlanet=[0,0,0,0]

		for i in range(self.numberOfStars):
			if self.tmpList[i].getType()=="m":
				self.medNumOfStars+=1
				for j in range(4):
					mediumStarPlanet[j] += self.tmpList[i].generatePlanet()[j]
			elif self.tmpList[i].getType()=="d":
				self.dwarfNumOfStars+=1
				for j in range(4):
					dwarfStarPlanet[j] += self.tmpList[i].generatePlanet()[j]
			else:
				self.giantNumOfStars+=1
				for j in range(4):
					giantStarPlanet[j] += self.tmpList[i].generatePlanet()[j]

		print("Dwarf stars are: ",self.dwarfNumOfStars)
		self.printHelper(mediumStarPlanet)
		print("Medium stars are: ",self.medNumOfStars)
		self.printHelper(dwarfStarPlanet)
		print("Giant stars are: ",self.giantNumOfStars)
		self.printHelper(giantStarPlanet)