def bubble_sort(arre):
    n=len(arre)
    for i in range(n):
        for j in range(0,n-i-1):
            if arre[j]>arre[j+1]:
                arre[j],arre[j+1]=arre[j+1],arre[j]
arre=[4,8,7,6,2,5]
bubble_sort(arre)
print(arre)

# insertionSort
def insertionSort(arre):
    print(arre)
    for a in range(1,len(arre)):
        b=a
        while b>0 and arre[b]<arre[b-1]:
            arre[b]=arre[b-1]
            b=b-1
insertionSort(arre)
print(arre)

# tuple
tuple=["vishal ","mohit","nitin"]
# for i in range( 0,len(tuple)):
#     print(tuple[i])

# tuple.append("vishal yadaw ")
# tuple.remove( "vishal ")
# tuple.extend( ["vishal ","yadaw"])
tuple.reverse()
print(tuple)
