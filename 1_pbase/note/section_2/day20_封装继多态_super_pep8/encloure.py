class A:
    def __init__(self, args):
        self.__p = args

    def __private_method(self):
        print("你好,我是私有方法:")

    def showA(self):
        print("self.__p=", self.__p)
        self.__private_method()

class B(A):
    def __init__(self):
        super().__init__(0)

    def myfun(self):
        pass
        # print("self.__p=", self.__p)  # 错的,不能使用私有方法
        # self.__private_method()  # 错的,不能调用基类的私有方法


b = B()
b.myfun()

a = A(100)
a.showA()
# 私有方法不能在类外部调用
# a.__private_method()
# 私有属性不能在外部使用
# a.__p -= 2
# print(a.__p)
