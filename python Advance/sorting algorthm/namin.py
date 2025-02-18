# # Sorting reverse
# L1=[1,5,9,8,4,7,6,2,3,0,]
# L1.sort(reverse=True)
# print(L1)
# # shorting 
# L1=[1,5,9,8,4,7,6,2,3,0,]
# L1.sort()
# print(L1)

def buble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1]=arr[j+1],arr[j]
arr=[1,2,3,5,6,98,8,7,4,5,6]
buble_sort(arr)
print(arr)

def bs(arre):
    a=len(arre)
    for i in range(a):
        for j in range(0,a-i-1):
            if arre[j]>arre[j+1]:
                arre[j],arre[j+1]=arre[j+1],arre[j]
arre=[1,2,5,8,2,3,6,4,7,8,9]
bs(arre)
print(arre)