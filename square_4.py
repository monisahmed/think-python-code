from swampy.TurtleWorld import*

def square(x,tut,angle):
    for i in range(4):
        fd(tut,x)
        lt(tut,angle)


def polygon(lenght,tut,angle,side):
    for i in range(side):
        fd(tut,lenght)
        lt(tut,angle)
    wait_for_user()


def poly(t,n,lenght):
    angle = 360.0/n
    for i in range(n):
        fd(t,lenght)
        lt(t,angle)
    wait_for_user()



world = TurtleWorld()
ct = Turtle()
poly(ct,7,50)
