

# 小张写的A类
class A:
    def __init__(self):
        self.name = "A"

# 小李写的B类
class B:
    def __init__(self):
        self.name = "B"


# 小王感觉小张和小李写的两个类自己可以用
class AB(A, B):
    def infos(self):
        print(self.name)  # 请问打印结果是什么?


ab = AB()
ab.infos()  # ????
ab2 = AB()
ab3 = AB()