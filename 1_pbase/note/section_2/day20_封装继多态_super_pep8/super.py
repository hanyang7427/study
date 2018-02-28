

class A(object):
    def hello(self):
        print("A类的hello(self)")


class B(A):
    def hello(self):
        print("B类的Hello(self)")

    def super_hello(self):  # 此方法用来调用基类的hello方法
        # super(B, self).hello()
        # 以上可以简写为:
        super().hello()

b = B()
b.hello()  # 调用B类的方法
# 调用基类方法:
super(B, b).hello()  # A类的hello 被调用 等同于 B.__base__.hello(b)
b.super_hello()  