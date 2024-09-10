import turtle

class Paddle(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.speed(0)
        self.setheading(90)
        self.penup()
        self.x = x
        self.y = y
        self.setposition(self.x, self.y) #sets the position of the paddles
        self.color("white")
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=5)#extends the turtle's size
        
    def move_up(self):
        self.fd(40)
        
    def move_down(self):
        self.bk(40)
        