# 快速排序
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i < pivot]
        more = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(more)

print(quicksort([3,2,4,6,5,1]))
# 桶排序
def tong(array):
    atong = [x for x in range(max(array))]
    for i in array:
        atong[i-1] = i
    return atong

print(tong([1,4,3,6,5,2,7,100]))
# 冒泡排序
def bubble_sort(array):
    L1 = array[:]
    L2 = []
    i = 0
    while i < len(array):
        j = 0
        while j < len(L1)-1:
            if L1[j]>L1[j+1]:
                L1[j],L1[j+1] = L1[j+1],L1[j]
            j += 1
        L2.append(L1[-1])
        del L1[-1]
        i += 1
    return L2


# 选择排序
def find_max(array,max_v=0):
    x= array[:]
    if not x:
        return max_v
    if max_v < x[0]:
        max_v = x[0]
        del x[0]
    else:
        del x[0]
    return find_max(x,max_v=max_v)
def xuanze_sort(array):
    L = []
    while True:
        a = find_max(array)
        L.append(a)
        try:
            array.remove(a)
        except:
            break
    return L
print(xuanze_sort([1,5,6,8,4,4,4]))
