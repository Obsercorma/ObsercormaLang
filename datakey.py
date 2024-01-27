import turtle as t

class DataKey:
    def __init__(self, x:float, y:float, data:tuple):
        self.x = x
        self.y = y
        self.data = data
    
    # 1 = II, 2 = OO, 3 = IO, 4 = OI
    def draw(self):
        offsetRotation = 90.0
        assert len(self.data) == 4, "DataKey.draw() requires a tuple of length 4."
        for d in range(0, len(self.data)):
            assert self.data[d] in (1, 2, 3, 4), "DataKey.draw() requires a tuple of 1, 2, 3, or 4."
            obj = t.Turtle()
            obj.hideturtle()
            obj.speed(15.0)
            obj.setx(self.x-50.0)
            obj.sety(self.y)
            obj.width(7.0)
            obj.right(90)
            obj.circle(radius=50.0)
            obj.penup()

            obj.setx(self.x)
            obj.sety(self.y)

            obj.left((45.0+(offsetRotation*d)))
            if self.data[d] == 1:
                offsetBar = 15.0
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
            elif self.data[d] == 2:
                # offsetBar = 20.0
                obj.forward(20.0)
                obj.right(90.0)
                obj.forward(-1.0)
                obj.pendown()
                obj.begin_fill()
                obj.circle(10.0)
                obj.end_fill()
            elif self.data[d] == 3:
                offsetBar = 10.0 #Draw circle first
                obj.forward(80.0)
                obj.left(90.0)
                # obj.forward(20.0)
                obj.begin_fill()
                obj.circle(10.0)
                obj.end_fill()
                obj.penup()

                obj.right(90.0)
                obj.forward(offsetBar)
                obj.left(90.0)

                obj.backward(20.0) # Draw bar after
                obj.pendown()
                obj.forward(40.0)
                obj.penup()
            else:
                offsetBar = 15.0
                obj.forward(70.0)
                obj.right(90.0)
                obj.backward(20.0)
                obj.pendown() # Draw bar first
                obj.forward(40.0)
                obj.penup()
                obj.backward(20.0)
                obj.left(90.0)
                obj.forward(offsetBar)
                obj.right(90.0)

                obj.backward(10.0) # Draw circle after
                obj.right(90.0)
                obj.backward(5.0)
                obj.begin_fill()
                obj.circle(10.0)
                obj.end_fill()


if __name__ == "__main__":
    data = (3, 3, 3, 3)
    x = 0.0
    y = 0.0
    dk = DataKey(x, y, data)
    dk.draw()
    t.done()
