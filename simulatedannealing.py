import random
import math

x1 = random.uniform (-10 , 10)
x2 = random.uniform (-10 , 10)

def bilangan1 (x1 , x2):
    bil = ((4-(2.1*x1**2) + ((x1**4)/3)) * (x1**2) + (x1*x2) + (-4+(4*(x2**2))*x2**2))
    return bil

temp = 100000
a    = 0.99
min  = 0.001
bilangan1(x1 , x2)

while (temp > min):
    x1 = random.uniform (-10 , 10)
    x2 = random.uniform (-10 , 10)
    bilangan2 = ((4-(2.1*x1**2) + ((x1**4)/3)) * (x1**2) + (-4+(4*(x2**2)) * x2**2))
    r = random.uniform(0 , 1)

    if (bilangan1 > bilangan2):
        bilangan1 = bilangan2
    else :
        if((math.exp((bilangan1-bilangan2)/temp)) > r):
            bilangan1 = bilangan2
        temp = temp*a

print "Nilai Minimum :" , bilangan1
