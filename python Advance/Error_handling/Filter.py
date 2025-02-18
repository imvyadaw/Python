# Filter
num=(1,2,3,4,5,6,7,8,9)
def fil(a):
    if a>5:
        return a
# out=filter(fil,(1,4,7,3,9))
out=filter(fil,(num))
print(list(out))

# Filter lambda 
names=["vishal","nitin","mohit","nishant"]
myobj=filter(lambda x:"v"in x,names)
print(list(myobj))

# filter 3 methods
veg=["banana","apple","carrote"]
def vegitable(x):
    return "e" in x
list_veg=(list(filter(vegitable,veg)))
print("This is a 'e' letter word =",list_veg)