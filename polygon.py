from swampy.TurtleWorld import*
from math import *

def poly(t,n,lenght):
    angle = 360.0/n
    for i in range(n):
        fd(t,lenght)
        lt(t,angle)
    wait_for_user()



def circle(t,r):
    circum = 2 * 3.1415 * r
    n = 50
    lenght = circum/n
    poly(t,n,lenght)



world = TurtleWorld()
ct = Turtle()
circle(ct,90)
