import multiprocessing
def wanquanshu(x):
    L = []
    for j in range(1,x):
        L2 = []
        for i in range(1,j):
            if j % i == 0:
                L2.append(i)
        if sum(L2) == j:
            L.append(j)
    print(L)
p1 = multiprocessing.Process(target = wanquanshu,args = (10000,))
p2 = multiprocessing.Process(target = wanquanshu,args = (10000,))
p2.start()
p1.start()
