import turtle
import random as rd

class Ball(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.speed(0)
        self.penup()
        self.color('white')
        self.shape("circle")
        self.ball_speed = 0.01
        self.headings = [0, 90, 180, 270]
        self.x = x
        self.y = y
        self.Vx = 5 # change in turtle x-axis position 
        self.Vy = 5 # change in turtle y-axis position
        self.setx(-self.x+42)
        self.setheading(rd.choice(self.headings))
        self.started = 0
        #self.headed = 0
        
    def move_ball(self):
        """moves the turtle with constant velocity in x and y"""
        self.setposition(self.xcor()+self.Vx, self.ycor()+self.Vy)
        self.started += 1
        
    def bounce_from_vertical_wall(self):
        """bounces the turtle of the wall"""
        if self.ycor() > self.y-15:
            #top wall
            self.Vy = -self.Vy #1.reverses the turtle vetical velocity 
            self.setposition(self.xcor()+self.Vx, self.ycor()+self.Vy)
        elif self.ycor() < -self.y+15:
            #floor 
            self.Vy = -self.Vy #1.
            self.setposition(self.xcor()+self.Vx, self.ycor()+self.Vy)
            
    def bounce_paddles(self):
        """bounces of the turtle the paddles"""
        self.Vx = -self.Vx #because the reflection of the paddles cause x to -x
        self.setposition(self.xcor()+self.Vx, self.ycor()+self.Vy)
        self.ball_speed *= 0.9 
        
    def reset_speed(self):
        self.ball_speed = 0.01     
        