import turtle as t


class StartIndexKey:
    def __init__(self, x: float, y: float, repeat: int = 1, offset: float = 15.0):
        assert repeat > 0 and repeat < 5, "Repeat must be between 1 and 4"
        self.x = x
        self.y = y
        self.repeat = repeat
        self.offset = offset

    def draw(self):
        offsetRadius = 5.0
        for i in range(self.repeat):
            obj = t.Turtle()
            obj.hideturtle()
            obj.penup()
            obj.speed(0)
            obj.setx(self.x)
            obj.sety(self.y + 50.0)
            obj.width(3.0)
            obj.right(0.0)
            obj.backward((200.0 - (self.offset * i)))
            obj.left(90.0)
            obj.backward((97.0 - (offsetRadius * i)))
            obj.right(105.0)
            obj.pendown()
            obj.circle(radius=(50.0 - (offsetRadius * i)), extent=-150.0)


class EndIndexKey:
    def __init__(self, x: float, y: float, invert: bool = False):
        self.x = x
        self.y = y
        self.invert = invert

    def draw(self):
        obj = t.Turtle()
        obj.hideturtle()
        obj.penup()
        obj.speed(0)
        obj.setx(self.x)
        obj.sety(self.y)
        obj.width(3.0)
        obj.right(90.0)
        obj.pendown()
        obj.forward(30.0)
        obj.circle(radius=15.0, extent=230.0)
        obj.penup()
        obj.right(90.0)
        obj.forward(10.0)  # draw NOT gate
        obj.pendown()
        obj.backward(20.0)
        obj.penup()

        if self.invert:
            obj.forward(30.0)
            obj.left(90.0)
            obj.forward(20.0)
            obj.begin_fill()
            obj.circle(radius=4.0)
            obj.end_fill()
            obj.right(90.0)

        obj.setx(self.x)
        obj.sety(self.y)
        obj.pendown()
        obj.left(40.0)
        obj.forward(30.0)
        obj.left(0.0)
        obj.circle(radius=10.0, extent=230.0)
        obj.penup()


if __name__ == "__main__":
    t.setup(width=800, height=800)
    t.title("Index Key")
    t.speed(0)
    t.tracer(0, 0)
    index = StartIndexKey(x=0.0, y=0.0, repeat=3, offset=15.0)
    index.draw()
    endIndex = EndIndexKey(x=0.0, y=0.0)
    endIndex.draw()

    t.update()
    t.mainloop()
