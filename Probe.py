import math

class Probe:
  def __init__(self, universe):
    self.universe = universe
    self.planetsExplored = 0
    self.totalDistance = 0
    self.amountOfFuel = 60000
    self.consumedFuel = 0
    self.totalStars = 0
    self.totalPlanets = 0
    self.lifeExists = False
    self.x = 0
    self.y = 0
    self.z = 0

    self.planetId= ''

  def getDistance(self,x1,y1,z1, x2,y2,z2):
    return math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)+(z2-z1)*(z2-z1))

  def visitPlanets(self, lifeCounter, minDistanceIndex):
    for k in self.universe.getList()[minDistanceIndex].getPlanets():
      lifeCounter = lifeCounter + 1
      self.totalPlanets+=1 # Total planet visited counter
      if k.getIntelligence(): #if intelligent life is detected then terminate it
        self.lifeExists=True
        self.planetId=k.getPlanetID() + str(lifeCounter)
        return True
    return False

  def fuelConsumption(self, minDistanceIndex):
    self.amountOfFuel = self.amountOfFuel + self.universe.getList()[minDistanceIndex].getReChargeAmount()
    self.amountOfFuel=self.amountOfFuel-(self.amountOfFuel * self.universe.getList()[minDistanceIndex].getChancesOfLife() * 100)
    if self.amountOfFuel< 0:
      self.amountOfFuel = 0
      return True
    return False

  def searchAlg(self):
    self.x = self.universe.getList()[0].x
    self.y = self.universe.getList()[0].y
    self.z = self.universe.getList()[0].z

    self.universe.getList()[0].setVisited()

    self.totalStars=1
    tmpx=self.x
    tmpy=self.y
    tmpz=self.z

    lifeCounter = 0

    for i in range(self.universe.getListLength()-1):
      tmpDistance = []
      for j in range(self.universe.getListLength()):
        if(self.universe.getList()[j].getVisited() == False):
          distance=self.getDistance(tmpx,tmpy,tmpz,self.universe.getList()[j].x,self.universe.getList()[j].y,self.universe.getList()[j].z)
          tmpTuple = (distance, j)
          tmpDistance.append(tmpTuple)

      minDistanceIndex = min(tmpDistance)[1]
      minDistance = min(tmpDistance)[0]
      self.universe.getList()[minDistanceIndex].setVisited()

      self.totalDistance = self.totalDistance + minDistance
      self.totalStars = self.totalStars + 1

      tmpx=self.universe.getList()[minDistanceIndex].x
      tmpy=self.universe.getList()[minDistanceIndex].y
      tmpz=self.universe.getList()[minDistanceIndex].z  
  
      # Consume fuel, if no fuel left, then return
      if(self.fuelConsumption(minDistanceIndex)):
        return
      # If find Life in the visited planets, returns
      if(self.visitPlanets(lifeCounter, minDistanceIndex)):
        return
      

  def printHelper(self):
    print("=======================================================")
    print(" Your origin was (" + str(self.x) + ',' + str(self.y) + ',' + str(self.z)+ ')')
    print(" Traveled "+ str(self.totalDistance) +" miles")
    print(" You have " + str(self.amountOfFuel) +" fuel remaining")        
    print(" Visited "+ str(self.totalStars) +" stars")
    print(" Explored "+ str(self.totalPlanets) +" planets ")
    if(self.lifeExists):
        print(" Found life on planet ",self.planetId)
    else:
        print("No life intelligent planet found")