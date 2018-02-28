
"""
   此模块用来演示覆盖run方法
"""
class Human:
    def say(self, what):
        print("说:", what)

    def run(self, speed):
        print("正在以", speed, "km/h速度奔跑!")


class Teacher(Human):
    def techer(self, language):
        print("老师正在教:", language)

    # def run(self, speed):
    #     print("老师正在以", speed, "米/分钟的速度走")


class Student(Teacher):
    def study(self, prog):
        print("正在学习", prog)

    def run(self, speed):
        print("走走跑跑还看手机，速度", speed)

    def walk(self, speed):  # 走的方法
        # self.run(speed)  # 调用自身
        self.__class__.__base__.run(self, speed)  # 借助于self调用父类的run


h1 = Human()
s1 = Student()
t1 = Teacher()

h1.run(5)
s1.run(7)  # 此时调用的是子类的覆盖版本的方法
t1.run(6)

# 子类调用基类的版本（原版本）方法
Human.run(s1, 10)

s1.walk(3)
