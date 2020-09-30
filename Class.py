class Myclass:
    i = 12345

print(Myclass.i)

class Complex:
    def __init__(self,realpart,imagepart):
        self.r = realpart
        self.i = imagepart
    def __del__(self):
        print('delete all')

x = Complex(3.0,-4.5)
print(x.r, x.i)
x = None


class Dog:
    def __init__(self,name):
        self.__name = name
        self.__tricks = []
    
    def add_tricks(self, tricks):
        self.__tricks.append(tricks)

    def printTricks(self):
        print(self.__name+str(self.__tricks))

d = Dog('小黑')
e = Dog('小白')
d.add_tricks('翻滾')
e.add_tricks('靜止')

d.printTricks()
e.printTricks()


#繼承實作
#Vehicle 父類別
class Vehicle:
    def __init__(self,name,engine):
        self.__name = name
        self.__engine = engine

    def getName(self):
        return self.__name

    def getEngine(self):
        return self.__engine

    def setEngine(self, engine):
        self.__engine = engine

class Electric:
    def __init__(self, PowerElectric):
        self.__PowerElectric = PowerElectric

    def getPower(self):
        return self.__PowerElectric
    def setPower(self, PowerElectric):
        self.__PowerElectric = PowerElectric

#Car 子類別
class Car(Vehicle, Electric):
    def __init__(self, name, engine, PowerElectric, auto):
        super().__init__(name, engine)
        self.setPower(PowerElectric)
        self.__auto = auto

    def getCarName(self):
        print('名字'+ self.getName())
        print('引擎'+ self.getEngine())
        print('電動車'+ self.getPower())

    def getAuto(self):
        print(self.__auto)

myCar = Car('特斯拉','磁電engine', '電力', '自動駕駛車')
myCar.getCarName()
myCar.getAuto()
    