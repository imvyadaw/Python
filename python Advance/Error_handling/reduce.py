# reduce
num2=[5,8]
from functools import reduce
r=reduce(lambda a,b:a*b,(num2))
print(r)

# Reduce function 
def sum_number(first,second):
    return first+second
result=reduce(sum_number,num2)
print(result)
