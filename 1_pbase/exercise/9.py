#!/usr/local/bin/python3
# class salary:
#     total_money = 5
#     # __slots__ = ["name","salary","month"]
#     def __init__(self,name,salary,month):
#         self.name,self.salary,self.month = name,salary,month
#     @classmethod
#     def total_salary(cls):
#         print("总工资为：",cls.total_money)
#     def h(self,cls):
#         print(cls.total_money)
# a1 = salary("wang",1000,3)
# a1.j = 100
# class mynumber:
#     """此类用于定义一个整形数字类，用于演示str函数重载"""
#     def __init__(self,value):
#         self.data = value
#     def __repr__(self):
#         return "mynumber(" + repr(self.data) + ")"
#     def __str__(self):
#         return str(self.data)
# print(mynumber(100))
# class mylist():
#     def __init__(self,*args):
#         self.data = [*args]
#     def __mul__(self, rhs):
#         return mylist(self.data * rhs)
#     def __rmul__(self,lhs):
#         return mylist(self.data * 2)
#     # def __imul__(self,rhs):
# class myint():
#     def __init__(self,x):
#         self.i = x
#     def __neg__(self):
#         return self.i +1
#     # def __mul__(self, other):
#     #     return mylist(5 * other.data)
# L1 = mylist(1,2,3)
# # L2 = L1.__mul__(3)# L1.__mul__(3)
# L3 = myint(3) * L1     # 3.__mul__(L1) L1.__rmul__(3)
# # print(L2.data)
# print(L3.data)

# a = 1
# a += 2
# a = a + 1
#
# ~0b1
# 补码
# import pdb
# pdb.set_trace()
# class mylist():  # 自定义list
#     def __init__(self, *x):
#         self.data = [*x]
#     def __add__(self, rhs):  # '+'右边
#         return mylist(*(self.data + rhs))
#     def __radd__(self, lhs):  # '+'左边
#         return mylist(*(self.data + lhs))
#     def __iadd__(self, rhs):  # '+='
#         self.data = self.data.append(rhs)
#
# print(mylist(1,2,3).data == mylist(1,2)+[3])

# class MyList():
#     def __init__(self,*args):
#         self.data = [*args]
#     def __add__(self,rhs):
#         return MyList(*(self.data + rhs))
#     def __iadd__(self,rhs):
#         self.data.extend(rhs)
#         return self
#     def __mul__(self,rhs):
#         return self.data * rhs
#     def __imul__(self,rhs):
#         self.data *= rhs
#         return self
#     def __len__(self):
#         return len(self.data)
#
# class OrderSet():
#     def __init__(self,*args):
#         self.data = set(sorted(list(args)))
#     def __and__(self,rhs):
#         return self.data & rhs.data
#     def __eq__(self,rhs):
#         if len(self.data) == len(rhs.data):
#             return False if False in map(lambda x,y:True if x == y else False,self.data,rhs.data) else True
#         else:
#             return False

# class Primes():
#     def __init__(self,end):
#         self.l = []
#         for i in range(2,end+1):
#             for j in range(2,i):
#                 if i % j == 0:
#                     break
#             else:
#                 self.l.append(i)
#     def __contains__(self,x):
#         if x in self.l:
#             print("zai ")
#             return True
#         else:
#             print("buzai")
#             return False

# class MyList():
#     def __init__(self, *args):
#         self.data = [*args]
#     def __setitem__(self, index, value):
#         self.data[index] = value
#     def __getitem__(self, index):
#         return self.data[index]
#     def __delitem__(self, index):
#         del self.data[index]
# a = MyList(1,2,3)
#
# print(a.data)

# class MyNum:
#     def __init__(self,b,e):
#         self.begin = b
#         self.end = e
#         self.curr = b
#     def __next__(self):
#         if self.curr <= self.end:
#             r = self.curr
#             self.curr += 1
#             return r
#         else:
#             raise StopIteration
#     # def __iter__(self):
#     #     self.curr = self.begin
#     #     return self
# it = MyNum(1,3)
# for i in it:
#     print(i)
# print([x for x in it])
import os
print(__file__)
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(os.path.dirname(os.path.abspath(__file__)))
# os.path.join(BASE_DIR, 'etc')