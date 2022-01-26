from matplotlib import pyplot
import math
def sinevalue(val):
    sum=0
    i=1
    b=0
    a=5
    while(abs(a)>0.00001):
        a=math.pow(-1,b)*(math.pow(val,i)/math.factorial(i))
        sum+=a
        i+=2
        b+=1
        
    return sum
x=[]
y=[]

j=0
while(j<=2*math.pi):
    x.append(j)
    
    y.append(sinevalue(j))
    j+=0.01
pyplot.plot(x,y)
pyplot.show()