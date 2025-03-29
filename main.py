import turtle as t
from rich import print as richPrint
from datakey import DataKey
from indexkey import StartIndexKey, EndIndexKey
from assemblykey import AssemblyKey
from translater import LetterKey, Translater
from random import randint

t.hideturtle()
t.setup(width=400, height=1080)

# circle = t.Turtle()

# circle.width(10)

# circle.circle(50.0)


def drawLine(width:float, height:float, x:float, y:float):
    obj = t.Turtle()
    obj.hideturtle()
    obj.up()
    obj.setx(x)
    obj.sety(y)
    obj.speed(30)
    obj.width(height)
    obj.right(0)
    obj.backward(270.0)
    obj.down()
    obj.forward(width)
    obj.up()

def drawFirstKey(x:float,y:float):
    obj = t.Turtle()
    obj.hideturtle()
    obj.speed(15)
    obj.setx(x)
    obj.sety(y)
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

t.bgcolor("lightgray")

#exemple de texte: Puisses tu réunir les connaissances.
text = "Puisse stureu nirles connai ssance s".split(" ") # groupement de 6 lettres

dataKeyObject = Translater(text[5])

initY = -300.0
pos = 0
for dataKey in dataKeyObject.translate():
    repeat = randint(1,4)
    dataFirstKey = dataKey[0]
    print(dataFirstKey)
    dataSecondKey = dataKey[1]
    for r in range(1, repeat):
        dataFirstKey = dataFirstKey[::-1]
        dataSecondKey = dataSecondKey[::-1]
        print(f"offsetting for '{dataKey[2]._letter}' {r} times")

    drawLine(340.0, 3.0, 95.0, initY+3.0+(110*pos))
    drawAssemblyKey = AssemblyKey(x=0.0, y=initY+0.0+(110*pos), data=dataKey[2].selectedPattern)
    drawAssemblyKey.draw()
    startIndex = StartIndexKey(x=60.0, y=initY+0.0+(110*pos), repeat=repeat, offset=8.0)
    startIndex.draw()
    endIndex = EndIndexKey(x=130.0, y=initY+3.0+(110*pos), invert=dataKey[2].useNotPattern)
    endIndex.draw()
    firstDataKey = DataKey(-60.0, initY+3.0+(110*pos), dataFirstKey)
    firstDataKey.draw()
    secondDataKey = DataKey(60.0, initY+3.0+(110*pos), dataSecondKey)
    secondDataKey.draw()
    pos += 1

ts = t.getscreen()
ts.getcanvas().postscript(file="text.ps")
richPrint("[green]\[DONE!][/green]")
t.exitonclick()