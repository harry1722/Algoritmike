
def identify(x):
    n=len(x)
    i=n-1
    while (i>0) and (x[i-1]>x[i]):
        i=i-1
    return i

def minimum(x,i):
    n=len(x)
    k=i
    for j in range(i+1,n):
        if (x[j]<x[k]) and (x[j]>x[i-1]):
            k=j
    return k
def swap(a,b):
    aux=a
    a=b
    b=aux
    return a,b

def reverse(x,left,right):
    i=left
    j=right
    while i<j:
       x[i],x[j]=x[j],x[i]  # other type of swap
       i=i+1
       j=j-1
    return x    

x=[6,3,0,9,4,8,7,5,2,1]
print “Digits of the initial number :",x
i=identify(x)
print "i=",i
k=minimum(x,i)
print "k=",k
x[i-1],x[k]=swap(x[i-1],x[k])
print “Sequence after swap:",x
x=reverse(x,i,len(x)-1)
print “Sequence after reverse:",x

