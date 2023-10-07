"""
About Dispatch: In Python, the @dispatch decorator is used to overload functions with different signatures. This is a common pattern in object-oriented programming where multiple methods can have the same name, but different parameters or argument types.
"""


from multipledispatch import dispatch

@dispatch(int,int)
def product(a,b):
    print('multiplication of 2 integers')
    return(a*b)

@dispatch(int, int, int)
def product(a,b,c):
    print('multiplication of 3 integers')
    return(a*b*c)

@dispatch(float, float, float)
def product(a,b,c):
    print('multiplication of 3 floats')
    return(a*b*c)

r = product(2,5)
print(r)

r2 = product(2,5,6)
print(r2)

r3 = product(2.6,5.9,6.1)
print(r3)

r4 = product(2.6,float(5),6.3) #we need to convert it in float first
print(r4)