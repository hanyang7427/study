class Human:
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age
    # def infos(self):
    #     print("我叫:", self.name,
    #           "我今年:", self.age, "岁")
    def say(self, what):
        print("说:", what)

    def run(self, speed):
        print("正在以", speed, "km/h速度奔跑!")

h1 = Human()
h1.say("天气真好!")
h1.run(5)

class Student(Human):
    # def say(self, what):
    #     print("说:", what)

    # def run(self, speed):
    #     print("正在以", speed, "m/分钟速度奔跑!")

    def study(self, prog):
        print("正在学习", prog)

s1 = Student()
s1.say("午餐咱们吃什么")
s1.run(7)
s1.study("Python3")


class Teacher:
    def techer(self, language):
        print("老师正在教:", language)


t1 = Teacher()
t1.techer("英文")

print("Teacher类的基类", Teacher.__base__)
print("Student类的基类", Student.__base__)
print("object类的基类", object.__base__)

t1.__class__.__base__


