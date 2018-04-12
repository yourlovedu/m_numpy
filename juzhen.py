import math
import random

def main():
    a=[[1,2],[3,4],[5,6]]
    print a
    b=[[2,5],[8,7]]
    print b
#print a*b
#a[0][0]=2
    print dot(a,b)
    w=randn(1,3)
    print w
    print w[0][2]
    print [[0 for x in range(2)] for y in range(1)]
    c=[[0,1,2],[3,4,5]]
    print c
    print argmax(c, y)
    print reshape(c,(3,2))
    print zeros((10,1))
    print zeros(c)
#print math.exp(a)


def dot(xx,yy):
    #print xx
    #print yy
    w =[[1 for x in range(len(yy[0]))] for y in range(len(xx))]
    for i in range(len(xx)):
        for j in range(len(yy[0])):
            temp=0
            for k in range(len(xx[0])):
                temp+=xx[i][k]*yy[k][j]
                #print temp
            w[i][j]=temp
    return w

def randn(xx,yy): #need to modify
    exp = 0 
    var = 1 
    #xx = random.normalvariate(exp, var) 
    return [[random.normalvariate(exp, var) for x in range(yy)] for y in range(xx)]

def zeros(shape):#need to modify
    if isinstance(shape[0],int):
        return [[0 for x in range(shape[1])] for y in range(shape[0])]
    else:
        return [[0 for x in range(len(shape[0]))] for y in range(len(shape))] 
        
def ones(shape):#need to modify
    if isinstance(shape[0],int):
        return [[1 for x in range(shape[1])] for y in range(shape[0])]
    else:
        return [[1 for x in range(len(shape[0]))] for y in range(len(shape))] 

#def zeros((xx,yy)):
#    return [[0 for x in range(yy)] for y in range(xx)]

def argmax(a, axis):
    max=0
    if axis==1:
        w=[[0 for x in range(len(a[0]))] for y in range(1)]
        for j in range(len(a[0])):
            for i in range(len(a)):
                if i==0:
                    max=a[i][j]
                    w[0][j]=i
                if a[i][j]>max:
                    max=a[i][j]
                    w[0][j]=i
    elif axis ==0:
        w=[[0 for x in range(len(a))] for y in range(1)]
        for j in range(len(a)):
            for i in range(len(a[0])):
                if i==0:
                    max=a[j][i]
                    w[0][j]=i
                if a[j][i]>max:
                    max=a[j][i]
                    w[0][j]=i
    return w

def exp(a):
    w=[[0 for x in range(len(a[0]))] for y in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            w[i][j]=math.exp(a[i][j])
    return w

def exp_m(a):
    w=[[0 for x in range(len(a[0]))] for y in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            w[i][j]=math.exp(-a[i][j])
    return w

def reshape(a,(xx,yy)):
    w=[[0 for x in range(yy)] for y in range(xx)]
    xxx=0
    yyy=0
    for i in range(xx):
        for j in range(yy):
            w[i][j]=a[xxx][yyy]
            yyy+=1
            if(yyy==len(a[0])):
                xxx+=1
                yyy=0
    return w

def add(a,b):
    w=[[0 for x in range(len(a[0]))] for y in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            w[i][j]=a[i][j]+b[i][j]
    return w
    
def multiply(a,b):
    w=[[0 for x in range(len(a[0]))] for y in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            w[i][j]=a[i][j]*b[i][j]
    return w
    
def multiply_c(b,a):
    w=[[0 for x in range(len(a[0]))] for y in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            w[i][j]=a[i][j]*b
    return w

def sub(a,b):
    w=[[0 for x in range(len(a[0]))] for y in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            w[i][j]=a[i][j]-b[i][j]
    return w

def sub_c(a,b):
    w=[[0 for x in range(len(a[0]))] for y in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            w[i][j]=a[i][j]-b
    return w
    
def div(a,b):
    w=[[0 for x in range(len(a[0]))] for y in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            w[i][j]=a[i][j]/b[i][j]
    return w
    
def div_c(a,b):
    w=[[0 for x in range(len(a[0]))] for y in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            w[i][j]=a[i][j]/b
    return w
    
def transpose(a):
    w=[[0 for x in range(len(a))] for y in range(len(a[0]))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            w[j][i]=a[i][j]
    return w
    
if __name__ == "__main__":
    main()
