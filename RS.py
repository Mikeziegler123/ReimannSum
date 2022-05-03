# Authors: Michael Ziegler, John Ziegler
# Purpose: A python script to perform double integral multivariable Riemann
# sum calculations.
# Date: May 3rd, 2022

import math

#INPUT
#z = lambda x,y: (x * y)
#p1x = 0.0
#p1y = 2.0
#p2y = 0.0
#p2x = 2.0
#squares = 4

z = lambda x,y: ( (1-((x*x)/4))-((y*y)/9) )
p1x = -1.0
p1y = 1.0
p2y = -2.0
p2x = 2.0  
squares = 4

#PRE-CALCULATIONS
deltaX = (p1y - p1x)/math.sqrt(squares)
deltaY = (p2x - p2y)/math.sqrt(squares)

if(deltaY < 0):
   deltaY = deltaY * -1
if(deltaX < 0):
   deltaX = deltaX * -1
    
deltaA = deltaX * deltaY

#start point: llc
llcX = p1x
llcY = p2y

#start point: urc
urcX = p1x + deltaX
urcY = p2y + deltaY

#start point: mp
mpX = p1x + (deltaX/2.0)
mpY = p2y + (deltaY/2.0)

#RIEMANN SUM
#llc
sum = 0
for i in range(0, int(math.sqrt(squares))):
    x_ij = llcX + deltaX * i
    for j in range(0, int(math.sqrt(squares))):
        y_ij = llcY + deltaY * j
        print("x_ij:", x_ij, " ", "y_ij:", y_ij)
        sum = sum + z(x_ij, y_ij)
Rsum = sum * deltaA
print("LLC approximation:", Rsum)

#urc
sum = 0
for i in range(0, int(math.sqrt(squares))):
    x_ij = urcX + deltaX * i
    for j in range(0, int(math.sqrt(squares))):
        y_ij = urcY + deltaY * j
        print("x_ij:", x_ij, " ", "y_ij:", y_ij)
        sum = sum + z(x_ij, y_ij)
Rsum = sum * deltaA
print("URC approximation:", Rsum)

#mp
sum = 0
for i in range(0, int(math.sqrt(squares))):
    x_ij = mpX + deltaX * i
    for j in range(0, int(math.sqrt(squares))):
        y_ij = mpY + deltaY * j
        print("x_ij:", x_ij, " ", "y_ij:", y_ij)
        sum = sum + z(x_ij, y_ij)        
Rsum = sum * deltaA
print(" MP approximation:", Rsum)   
