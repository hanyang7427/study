#!/usr/local/bin/python3
L = []


# def read_name(x):
#     x.append(input("输入姓名："))
#
#
# read_name(L)
# print(L)
# L1 = []
#
#
# def read_name_return(x):
#     L1.append(input("输入姓名："))
#     return L1
#
#
# print(read_name_return(L1))

def get_op(op):
    def my_add(x, y):
        return x+y

    def my_mul(x, y):
        return x*y
    if op == "+":
        return my_add
    if op == "*":
        return my_mul


a = int(input("输入第一个数："))
b = int(input("输入地二个数："))
operator = input("输入方式")
fn = get_op(operator)
print("结果是：", fn(a, b))
