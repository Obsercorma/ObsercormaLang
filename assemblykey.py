import turtle as t

class AssemblyKey:

    # (rq, ope)
    MUL_PATTERN = (0, 1)
    DIV_PATTERN = (0, 0)
    ADD_PATTERN = (1, 1)
    SUB_PATTERN = (1, 0)

    # [0] of data define if math operation is '*,/' or '+,-', [1] of data define if operation is which operator will be used
    def __init__(self, x:float, y:float, data:tuple):
        assert len(data) == 2, "AssemblyKey.__init__() requires a tuple of length 2."
        assert data[0] in (0, 1), "AssemblyKey.__init__() requires a tuple of 0 or 1."
        assert data[1] in (0, 1), "AssemblyKey.__init__() requires a tuple of 0 or 1."
        self.x = x
        self.y = y
        self.data = data

    def _is_MUL_OPE(self)->bool:
        return self.data == self.MUL_PATTERN

    def _is_DIV_OPE(self)->bool:
        return self.data == self.DIV_PATTERN
    
    def _is_ADD_OPE(self)->bool:
        return self.data == self.ADD_PATTERN
    
    def _is_SUB_OPE(self)->bool:
        return self.data == self.SUB_PATTERN

    def _is_R_OPE(self)->bool:
        return self.data[0] == 1

    def _is_Q_OPE(self)->bool:
        return self.data[0] == 0

    def draw(self)->None:
        obj = t.Turtle()
        obj.hideturtle()
        obj.speed(15)
        obj.setx(self.x)
        obj.sety(self.y)
        obj.width(7.0)

        obj.begin_fill() # Draw the center as a circle
        obj.circle(radius=15.0)
        obj.end_fill()
        obj.penup()

        obj.left(90.0)
        obj.backward(60.0)
        obj.left(135.0)
        obj.forward(25.0)
        obj.pendown()
        obj.backward(25.0)
        obj.penup()
        #stateOPE = '' # 'r' is ADD or SUB, 'q' is MUL or DIV
        if self._is_R_OPE(): # Draw Bar if ADD or SUB
            obj.forward(25.0)
            obj.left(90.0)
            obj.forward(20.0)
            obj.right(90.0)
            obj.pendown()
            obj.backward(25.0)
        elif self._is_Q_OPE(): # Draw Circle if MUL or DIV
            obj.forward(7.0)
            obj.right(90.0)
            obj.backward(20.0)
            obj.pendown()
            obj.begin_fill()
            obj.circle(7.0)
            obj.end_fill()
            obj.left(90.0)
        
        obj.penup()
        obj.right(45.0)

        obj.setx(self.x)
        obj.sety(self.y)
        obj.left(90.0)
        obj.forward(60.0)
        obj.pendown()
        obj.backward(150.0)

        obj.right(45.0)
        obj.backward(25.0)
        obj.penup()

        if self._is_ADD_OPE() or self._is_MUL_OPE():
            obj.right(90.0) # Draw Bar if ADD or MUL
            obj.forward(20.0)
            obj.left(90.0)
            obj.pendown()
            obj.forward(25.0)
        elif self._is_SUB_OPE() or self._is_DIV_OPE():
            # obj.right(90.0) # Draw Circle if SUB or DIV
            obj.forward(4.0)
            obj.right(90.0)
            obj.forward(20.0)
            obj.pendown()
            obj.begin_fill()
            obj.circle(7.0)
            obj.end_fill()
            obj.left(90.0)





if __name__ == "__main__":
    t.setup(width=800, height=800)
    t.title("Assembly Key")
    t.speed(15)
    assembly = AssemblyKey(x=0.0, y=0.0, data=AssemblyKey.SUB_PATTERN)
    assembly.draw()
    t.update()
    t.mainloop()