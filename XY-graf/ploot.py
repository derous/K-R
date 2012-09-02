from modulXY import plot1
import math

def sinus_pow2(x):
    return math.sin(x)**2

lines = [
    sinus_pow2,# mozhno ukazivat imya svoej funcii
    lambda x: x**0.5, # mozhno v odnu strochku napisat' funciju pramo tut
    math.log, # mozhno ukazat' lubuju mat func Python

]
plot1(lines, 1, 9, 0.1)
#plot1([math.sin], 2, 9, 0.1)

