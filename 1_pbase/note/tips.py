# ——————————————————————   取余   ——————————————————————————
# 一个大秒数，对60取余，结果一定小于60，为秒
# 一个大秒数，对60*60(一小时)取余，结果一定小于3600s(一小时)，为分
# 一个大秒数，对60*60*24(1天)取余，结果一定小于1天，为小时
# 10e5秒是多少天：        10e5 // (60*60*24)
# 10e5秒去掉天剩所少秒：   10e5 % (60*60*24)
# 10e5秒去掉天剩下的秒是多少小时：    10e5 % 60*60*24 // (60*60)

# ———————————————————— exec和eval区别 ———————————————————————
# print(exec("1+2"))    --> None    "1+2"被当做表达式执行，表达式1+2有返回值
# print(eval("1+2"))    --> 3       "1+2"被当做语句执行，语句1+2没有返回值

# ——————————————————————   进制   ——————————————————————————
# 1、二进制(bin),八进制(oct),十进制(dec),十六进制(hex)
bin(255) == '0b11111111'
oct(8)   == '0o10'
hex(16)  == '0x10'

# 2、几进制不出现几
# 0b1101010  -> 不出现2
# 0o3453457  -> 不出现8
# 0x129DEEA  -> 不出现F

# 3、
# 3位bin可以代表1位oct
# 000~111   -> 0~7
# 4位bin可以代表1位hex
# 0000~1111 -> 0~E

# bin 转 oct
# bin:  110  111  ->  0b110111
# oct:   5    7   ->  0o57

# bin 转 hex
# bin:  1101  1001  ->  0b11011001
# oct:   13     9   ->  0xd9
# 10:A, 11:B, 12:C 13:D 14:E 15:F

# 4、dec 转 bin       dec 转 oct
# 对2取余倒过来     对8取余倒过来

# 5、bin 转 dec
#   1       0       1       0
# 1*2^0 + 0*2^1 + 1*2^2 + 0*2^3

# 赋值(=)前边是变量，赋值(=)后边一定是一个表达式

# —————————————————————————————————————— 字符串或列表操作 ————————————————————————————————
# 列表转字符串
# 列表的元素必须是字符串
# ['a','b','c']
# 'abc'
''.join(['a','b','c'])

# 生成排好序的字符串
s = "AMCBJ"
''.join(sorted(s))

# 字符串以特定分隔符转列表
# '123x456x789'
# ['123','456','789']
'123x456x789'.split(sep='x')

# 去除字符串中的逗号
'1,2,3'.replace(',','')

# 反向打印
s = 'ABC'
for i in reversed(s):
    print(i)
# 生成反向列表
L = [100, 200, 300]
L2 = [x for x in reversed(L)]


# 两个变量 + 一个循环的字典推导式
# {'tom': 1, 'jerry': 2, 'sz': 3}
# x和y的个数可以不相等，缺少的不生成
{x:y for x,y in zip(["tom","jerry","hans"],[1,2,3])}

# 两个变量 + 嵌套循环的列表推导式
# [1+4,2+4,3+4 , 1+5,2+5,3+5]
# x和y的个数可以不相等，遍历所有可能
[x+y for x in [1, 2, 3] for y in [4, 5]]
list(map(lambda x:[x+y for y in (1,2)],(2,3)))

# 查看环境变量
help("__main__")
dir()

# 只能加表达式
# 赋值(=)必须加表达式
x = True if 1==1 else False
# lambda本身是一个表达式
# lambda的冒号(:)后加表达式或加有返回值的语句
lambda x:print(x)

# return后必须加表达式或语句
# 加语句时是执行了语句，并返回该语句返回的值
# return print(x)     # 执行了print(x)并返回print(x)的返回值(None)
# eval()的source必须为表达式

# 求素数
for i in range(3,10):
    for j in range(2,i):
        if i % j == 0:
            break           # else和for下的break配合，用来确保for下的语句全部执行\
else:                       # 当执行到else时，说明for下的break没有执行，说明所有的取余都不为0
    print(i,"是素数")

# ———————————————————————— while死循环 vs 递归 ————————————————————————
# 需要重复执行的语句可以放到死循环或递归函数里，使用break(while循环)和return(递归)控制结束条件
# while死循环重复执行的语句写在while语句块下   递归函数重复执行的语句写在函数里
# while死循环 用if break控制退出             递归用if return控制退出
# while 自带跳转属性                       递归用return f()跳转
# x = 1                                     def f(x):
# while True:                                   if x = 100:
#     if x < 100:                                   return "something"
#         break                                 x = x - 1
#     i += 1                                    return f(x)

# ————————————————————————— 闭包closure ——————————————————————
# 函数工厂：把参数传给函数工厂，函数工厂返回一个指定化函数
# 函数工厂例：
def outer(x):           # outer函数为一个函数工厂，x为工厂接收的参数
    def inner(y):       # 特点1，内嵌一个函数
        return x*y      # 特点2，内嵌的函数使用了外部函数的变量(x)
    return inner        # 特点3，外部函数返回值为内嵌函数
# 闭包：接收了函数工厂根据其收到的参数生产的函数，叫做闭包(闭包包括函数和作用域)
# 闭包例：
myclosure = outer(3)    # myclosure绑定的对象为一个闭包，它是函数工厂(outer)根据参数3制定的函数
myclosure(2)            # 将2传给闭包函数，等同于outer(3)(2)
# 什么时候使用闭包：当希望用一个函数生成制定的函数时

# —————————————————————————   装饰器  —————————————————————————
# 是一种函数工厂，假设fn绑定到一个函数，将这个函数传给装饰器，fn绑定到装饰器返回的函数
# 在函数工厂内部可已调用fn这个函数，给fn加一些功能
def outter(fn):
    def inner(y):
        return fn(y)+1
    return inner
@outter
def fn(x):
    return x+1
print(fn(1))

# —————————————————————————— 只能访问的全局变量 ——————————————————————————————
a = 1
def h():
    b = a       # 此句表示表示是a是一个全局变量且以后只能读取，不能再声明为全局或修改
                # 可以理解为一种特殊的全局变量

# ——————————————————————————— 传参：值传递和引用传递 ————————————————————————————
def f(x):pass
b = 1
a = [1,2]
# 不可变参数用值传递
f(b)
# 可变参数是用引用传递
f(a)

# ——————————————————————————— 传参 ————————————————————————————
# 各种形式的形参位置有要求
# 位置形参 > 星号元组形参(*args) > 命名关键字形参 > 双星号字典形参(**kwargs)

# ————————————————————————— 花式传参 ——————————————————————————
# *args/**kwargs作为实参传给函数时：
print(*(1,2,3),**{"end":" "})
# f(*(1,2,3))           表示把(1,2,3)元组拆开传给一个函数，print(*(1,2,3))=print(1,2,3)
# f(**{"end":"↲"})      表示把{"end":"↲"}字典改成end="↲"传给一个函数，print(1,2,end='↲',sep='→')=print(1,2,**{"end":"↲","sep":"→"})
# *args/*kwargs作为形参时：
# def f(*args,x)        把*args到x之间传来的参数全部收集到args，args在函数内部为一个元组，注意x必须是一个关键字参数
# def f(**kwargs)       把**kwargs之后所有传来的所有关键字参数收集到kwargs，kwargs在函数内部是一个字典，注意**kwargs之后不能加任何形参

# —————————————————————— a += 1 和 a = a+1 ——————————————————————
# a为不可变类型，做完这两个操作id(a)均发生了变化
# 两种操作均会创建一次和释放一次对象
# —————————————————————— a+=[1] 和 a=a+[1] ——————————————————————
# a为可变类型时，a += [1] id(a)不变， a = a + [1] id(a)会变
# a += [1] 不会创建也不会释放对象，只是对原来的对象修改，a绑定到同一个对象

# ————————— 浅拷贝 ————————————————————————————— 深拷贝 ———————————————
# a = [ xxxx, [ yyyy ] ]                # a = [ xxxx, [ yyyy ] ]
#         ➘       ⤓                     #         ➘      ⤓
#         xxxx    ⤓                     #         xxxx  yyyy(a使用一个)
#               yyyy(a和b使用同一个)      #         xxxx  yyyy(b使用一个)
#         xxxx    ⤒                     #         ➚      ⤒
#         ➚       ⤒                     # b = [ xxxx, [ yyyy ] ]
# b = [ xxxx, [ yyyy ] ]

# —————————————————————— repr和eval ————————————————————————
# s == eval(repr(s))        always True
# 有一个对象s
# s = ["a",{1:1,2:2},(1,2,3),{4,5,6},False,None,3.14,[1]]
# eval(s)           # 出错不能创建s对象
# eval(repr(s))     # 不出错，返回s对象

# range(10000) 优于 [x for x in range(10000)]
# range(10000)用一个生成一个(lazy produce)
# [x for x in range(10000)]全部生成，占用内存


# 重复执行的可以用for 递归函数
# 遍历可以用for 高阶函数
# 判断可以用快速条件表达式

# ——————————————————————— 一行一行遍历文件 ————————————————————
# f为可迭代对象，每次返回一个f.readline()
with open('file','r') as f:     # 也可以是rb
    for i in f:                 # i为每一行带'\n'
        print(i.strip())        # strip去掉空白字符(\n)
# 读所有
f.read()
# 读一行
f.readline()

# 重载和重写
# python中用变量名标识一个方法，一个名字就对应一个方法(这种叫做重写)
# 用变量名和参数个数或参数顺序，共同标识方法(叫做重载)
# 可以理解为重写只用方法名确定一个唯一的方法，重载用方法名和参数确定一个唯一的方法
# 例重载 示意代码 python不支持重载
# class A()
#     def f(x):
#         pass
# class B(A):
#     def f(x,y):
#         pass
# b = B()
# b.f(1,2) vs b.f(1)

# 10进制数转换成2进制，去掉0b，格式化成固定位数(补0)
('{0:0>'+str(x)+'}').format('{0:b}'.format(i))
# format位置
'xx{1}xx{0}xx'.format('aa','bb')    # 'xxbbxxaaxx'


# py文件变成pyc(字节码)cd ..
# python3 -m py_compile *.py
# pyc在 __pycache__目录里

# sorted
# key指定依据
L = [1,4,3,6,2,5]
L1 = [1,3,2,4,6,5]
sorted(L,key=L1.index)  # key指定一个函数
# 给L排序，以L1的索引为依据，1在L1中的索引为0,4在L1中的索引为4,3在L1中的索引为1，以此类推
# 结果为
#               [1, 3, 2, 4, 6, 5]
# in L1.index -> 0  1  2  3  4  5

# ————————————————————————————  pickle序列化  ——————————————————————————
import pickle
# 序列化
f = open('dump.txt','wb')
d = dict(name='Bob',age=20,score=88)
pickle.dump(d,f)
f.close()
# 反序列化
f = open('dump.txt','rb')
d = pickle.load(f)
f.close()
# ——————————————————————————————  json序列化  ————————————————————————————
# JSON类型        Python类型
# {}             dict
# []             list
# 'string'       str
# 123.456        int或float
# true/false     True/False
# null           None
import json
# 序列化
d = dict(name='Bob',age=20,score=88)
json.dumps(d)           # '{"score": 88, "name": "Bob", "age": 20}'
json_str = '{"score": 88, "name": "Bob", "age": 20}'
json.loads(json_str)    # {'score': 88, 'name': 'Bob', 'age': 20}
# 注：json标准规定json编码是utf-8,所以我们总是能正确的在Python的str与json的字符串之间转换
# ——————————————————————————————— 当要序列化的对象是自定义类 ——————————————————————
class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
s = Student('Bob',20,88)
# 序列化
# 将s(自定义类的实例传给default指定的函数)
print(json.dumps(s,default=lambda obj:obj.__dict__))
# 反序列化
def dict2student(d):
    return Student(d['name'],d['age'],d['score'])
json_str = '{"age":20,"score":"88","name":"Bob"}'
print(json.loads(json_str,object_hook=dict2student))

# ———————————————————————— 格式化输出时间 ————————————————————————————————————
import time
time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
# 打印当前时间
time.ctime()

# ———————————————————————— os模块路径拼接 ——————————————————————————
import os
# 路径拼接
path = os.path.join('/etc','passwd')
# 显示文件的绝对路径
os.path.abspath(__file__)
# 取目录
os.path.dirname('/etc/passwd')  # ---> /etc
# 取目录
os.path.dirname('/etc/network/')  # ---> /etc/network

# —————————————————— 包 模块 函数的导入 ——————————————————
# sys.path 中包含/path/to/package
# tree /path/to/package
# package/
# ├── mymod.py        --> def f1
# └── study
#     ├── __init__.py
#     └── en.py       --> def f2
# 导入包会执行包内的__init__.py
# 导入模块的本质是在当前文件执行被导入包的内容
# import cp                       错误,不能直接导入子包中的模块
# import mymod ; mymod.fn()       正确
# import study.en ; study.en.f2   正确
# from study import en ; en.f2    正确

# ————————————————————————————  ————————————————————————————
# >>> a ='s\-a'
# >>> a
# 's\\-a'
# >>> print(a)
# s\-a
# >>> repr(a)
# "'s\\\\-a'"
# >>> r's\-a'           # r''防止转义
# 's\\-a'

# ———————————————————————————— global陷阱 ————————————————————————————
# a = 1
# def f():
#     a = a + 1
# f()
# UnboundLocalError: local variable 'a' referenced before assignment(在赋值之前引用了)

# ———————————————————————————— super ————————————————————————————
# 当一个类继承自两个类是，访问相同的属性时，访问靠前的类的属性
# class A():                      class A():
#     x='A'                           x='A'
# class B():                      class B():
#     x='B'                           x='B'
# class C(A,B):                   class C(B,A):
#     pass                            pass
# c=C()                           c=C()
# super(C,c).x  # A               super(C,c).x  # B


enumerate([1,2,3])
