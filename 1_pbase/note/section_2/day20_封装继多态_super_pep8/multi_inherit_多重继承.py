

class Car:  # 汽车类
    def run(self, speed):
        print("汽车以", speed, "km/h的速度行驶")


class Plane:  # 飞机类
    def fly(self, height):
        print("在海拔", height, "米高度飞行!")


class PlaneCar(Car, Plane):
    """  PlaneCar类 同时继承自汽车和飞机"""


pl = PlaneCar()
pl.fly(10000)
pl.run(250)

