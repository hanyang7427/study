#!/usr/local/bin/python3
#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1
def local_line(L,space=0):
    print(" " * space,end="")
    for x in L:
        print(x,end=' ')
    print()

def next_line(L):
    out_L = []
    if L:
        out_L.append(L[0])
    if len(L) >= 2:
        for j in range(len(L)-1):
            out_L.append(L[j]+L[j+1])
    if L:
        out_L.append(L[-1])
    return out_L
L = [1]
for i in range(6):
    local_line(L,6-i-1)
    L = next_line(L)