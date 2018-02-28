#!/usr/local/bin/python3
# 输入数据

L = []
counter = 0
while True:
    s = input("输入信息(姓名,年龄,成绩)：")
    if s == '':
        break
    L.append(s)
    counter += 1
L2 = []
for i in range(counter):
    L2.append({x:y for x,y in zip(["姓名","年龄","成绩"],L[i].split(sep=','))})
# print(L2)
# def myfn(x):
#     return x["成绩"]
# print(sorted(L2,key=(lambda x:x["成绩"]),reverse=True))

# # 数据加索引
def porcess_data(field):
    processed_data = []
    if field == '成绩':
        for i in range(counter):
            processed_data.append(L2[i].get("成绩")+str(i))
        return processed_data
    if field == '年龄':
        for i in range(counter):
            processed_data.append(L2[i].get("年龄")+str(i))
        return processed_data
# # 返回排序和对应索引
def sort(sort_mode):
    def score_asc():
        L = []
        sorted_L = sorted(porcess_data("成绩"))
        for i in range(counter):
            L.append([sorted_L[i][:-1],sorted_L[i][-1]])
        return L
    def age_asc():
        L = []
        sorted_L = sorted(porcess_data("年龄"))
        for i in range(counter):
            L.append([sorted_L[i][:-1],sorted_L[i][-1]])
        return L
    if sort_mode == "成绩升序":
        return score_asc()
    if sort_mode == "年龄升序":
        return age_asc()
# print(sort("年龄升序"))
# print(sort("成绩升序"))

print("+----------+----------+----------+")
print("|"+"name".center(10)+"|"+"age".center(10)+"|"+"score".center(10)+"|")
print("|----------+----------+----------|")
for i in sort("年龄升序"):
    print("|" + L2[int(i[1])]["姓名"].center(10) + "|" + i[0].center(10) + "|" \
          + L2[int(i[1])]["成绩"].center(10) + "|")
print("|----------+----------+----------|")

print("+----------+----------+----------+")
print("|"+"name".center(10)+"|"+"age".center(10)+"|"+"score".center(10)+"|")
print("|----------+----------+----------|")
for i in sort("成绩升序"):
    print("|" + L2[int(i[1])]["姓名"].center(10) + "|" + L2[int(i[1])]["年龄"].center(10) \
          + "|" + i[0].center(10) + "|")
print("|----------+----------+----------|")