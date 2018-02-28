#!/usr/local/bin/python3
# import math
import pickle
# import pdb
# pdb.set_trace()
L = []


class Student(object):
    def __init__(self, *args, name='', age='', score=''):
        if args:
            self.name, self.age, self.score = args
        else:
            self.name, self.age, self.score = name, age, score

    def infos(self):
        print("|"+self.name.center(10) +
              "|"+self.age.center(10) +
              "|"+self.score.center(10)+"|")


def save():
    with open("stu", "wb") as f:
        pickle.dump(L, f)


def load():
    with open("stu", "rb") as f:
        global L
        L = pickle.load(f)


def modify():
    global L
    name = input("修改谁？：")
    L = list(map(lambda x: Student(*(input("修改为：").split(","))).__dict__ if x["name"] == name else x, L))


def dels():
    name = input("删除谁？：")
    L.remove(*(list(filter(None, map(lambda x: x if x["name"] == name else None, L)))))


def adds():
    while True:
        try:
            stu = Student(*(input("输入学生信息：").split(",")))
        except:
            break
        L.append(stu.__dict__)


def sorts():
    s = input("asc or desc：")
    global L
    if s == "asc":
        L = list(sorted(L, key=lambda x: x["score"]))
    if s == "desc":
        L = list(sorted(L, key=lambda x: x["score"], reverse=True))


def prints():
    print("|---name---+---age----+--score---|")
    for i in L:
        Student(**i).infos()
    print("|----------+----------+----------|")


d = {"a": adds, "d": dels, "m": modify, "p": prints, "w": save, "l": load, "s": sorts}

try:
    while True:
        print("a) 添加\nd) 删除\nm) 修改\np) 打印\nw) 保存\nl) 加载\ns) 排序")
        d[input("输入执行的任务：")]()
except:
    print("程序结束")
