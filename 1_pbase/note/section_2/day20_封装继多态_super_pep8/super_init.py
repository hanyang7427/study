

# file : super_init.py
# 此示例演示如何显示调用构造方法


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def infos(self):
        print("姓名:", self.name, "年龄:", self.age)


class Student(Human):
    def __init__(self, name, age, score):
        super(Student, self).__init__(name, age)
        self.score = score

    def infos(self):
        print("姓名:", self.name,
              "年龄:", self.age,
              "成绩:", self.score)


class Doctor(Student):
    def __init__(self, n, a, s, grad):  # grad"学位"
        super().__init__(n, a, s)
        self.grad = grad

h1 = Human("张三", 20)
h1.infos()

s1 = Student("李四", 30, 100)
s1.infos()