import math
class ExperimentalData:

      def __init__(self, gun, cartridgeCalibre,bulletRound,projectileVelocity,building,buildingHeight,gravity):
          self.gun = gun
          self.cartridgeCalibre = cartridgeCalibre
          self.bulletRound = bulletRound
          self.projectileVelocity = projectileVelocity
          self.building = building
          self.buildingHeight = buildingHeight
          self.gravity = gravity
      def getTime(self) :
            return (round(math.sqrt((2* self.buildingHeight)/self.gravity)))
      def getDistance(self):
          return(self.projectileVelocity * self.getTime())
      def run(self):
           print(f"If you shoot a {self.bulletRound} with a {self.gun} using a {self.cartridgeCalibre} cartridge from the {self.building} building , that mesures {self.buildingHeight} meters, it will take {self.getTime()} seconds till the bullet traveling at {self.projectileVelocity } m/s lands at {self.getDistance()} meters.")


          
#myData = ExperimentalData( "SV-98 bolt-action sniper rifle","7.62x54mmR",865,"7.62x54R LPS gzh,","30 St. Mary Axe", 179.8015,9.8 )
