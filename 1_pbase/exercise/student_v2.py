#!/usr/local/bin/python3

# [{"姓名":"sz","年龄":"18","成绩":"100"}, ...]
def writes():
    with open("stu",'w') as f:
        f.writelines(L)
# def reads():
#     with open("stu","r") as f:
#         f.readlines(L)
L = []
def adds():
    while True:
        s = input("输入添加的学生信息(姓名，年龄，成绩)：")
        if s:
            L.append({x:y for x,y in zip(["姓名","年龄","成绩"],s.split(sep=","))})
        else:
            break

def dels():
    global L
    s = input("输入删除的学生姓名：")
    def f(x,y):
        if x["姓名"] == y:
            return None
        else:
            return x
    L = list(filter(None,list(map(f,L,((s+"0")*len(L)).split(sep="0")))))
import pdb
def prints():
    def proc():
        for i in (L):
            print("|"+i["姓名"].center(10)+"|"+i["年龄"].center(10)+"|"+i["成绩"].center(10)+"|")
    print("+----------+----------+----------+")
    print("|" + "name".center(10) + "|" + "age".center(10) + "|" + "score".center(10) + "|")
    print("|----------+----------+----------|")
    proc()
    print("|----------+----------+----------|")

def sorts():
    global L
    s = input("输入排序方式(asc,desc)：")
    if s == "asc":
        L = sorted(L,key=lambda x:x["成绩"])
        prints()
    if s == "desc":
        L = sorted(L,key=lambda x:x["成绩"],reverse=True)
        prints()
# def modfs():
#     def proc(x):

while True:
    print("1) 添加学生信息                     ")
    print("2) 删除学生信息                     ")
    print("3) 修改学生信息                     ")
    print("4) 排序学生信息                     ")
    print("6) 显示学生信息                     ")
    print("7) 写入学生信息                     ")
    print("8) 退出                     ")
    a = int(input("输入执行的任务："))
    if a == 1:
        adds()
    if a == 2:
        dels()
    if a == 3:
        pass
    if a == 4:
        sorts()
    if a == 6:
        prints()
    if a == 7:
        writes()
        break
    if a == 8:
        break