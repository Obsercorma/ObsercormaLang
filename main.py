import turtle as t

t.hideturtle()

# circle = t.Turtle()

# circle.width(10)

# circle.circle(50.0)


def drawLine():
    obj = t.Turtle()
    obj.hideturtle()
    obj.setx(0.0)
    obj.speed(15)
    obj.sety(0.0)
    obj.width(7.0)
    obj.penup()
    obj.right(0)
    obj.backward(270.0)
    obj.pendown()
    obj.forward(400)
    obj.penup()

def drawFirstKey(x:float,y:float):
    obj = t.Turtle()
    obj.hideturtle()
    obj.speed(15)
    obj.setx(x)
    obj.sety(y)
    # obj.right(0)
    # obj.backward(50.0)
    obj.right(90)
    obj.width(7.0)
    obj.circle(radius=50.0)
    obj.penup()

dataKey = (1, 2, 3, 4) # 1 = II, 2 = OO, 3 = IO, 4 = OI

def drawDataKey(x:float,y:float, data:tuple):
    offsetRotation = 90.0
    for d in range(0, len(data)):
        obj = t.Turtle()
        obj.hideturtle()
        obj.speed(15.0)
        obj.setx(x)
        obj.sety(y)
        obj.width(7.0)
        obj.penup()
        obj.left((45.0+(offsetRotation*d)))
        if data[d] == 1:
            offsetBar = 20.0
            obj.forward(70.0)
            obj.right(90.0)
            for repbar in range(1, 3):
                obj.penup()
                obj.backward(20.0) 
                obj.pendown()
                obj.forward(40.0) # width of the bar
                obj.penup()
                obj.backward(20.0)
                obj.left(90.0)
                obj.forward(offsetBar)
                obj.right(90)
                # obj.right(90.0)
                # obj.forward((offsetBar*repbar))
        elif data[d] == 2:
            # offsetBar = 20.0
            obj.forward(20.0)
            obj.right(90.0)
            obj.forward(-1.0)
            obj.pendown()
            obj.begin_fill()
            obj.circle(10.0)
            obj.end_fill()
        elif data[d] == 3:
            pass
        else:
            pass

def drawIndex(repeat=1, offset=15.0):
    offsetRadius = 10.0
    for i in range(repeat):
        obj = t.Turtle()
        obj.hideturtle()
        obj.speed(15)
        obj.setx(0.0)
        obj.sety(0.0)
        obj.width(7.0)
        obj.penup()
        obj.right(0.0)
        obj.backward((200.0-(offset*i)))
        obj.left(90.0)
        obj.backward((97.0-(offsetRadius*i)))
        obj.right(105.0)
        obj.pendown()
        obj.circle(radius=(100.0-(offsetRadius*i)), extent=-150.0)


drawLine()
drawFirstKey(-100.0,0.0)
drawDataKey(-50.0, 0.0, (2,2,2,2))
drawIndex(repeat=4)

t.exitonclick()