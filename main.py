import turtle
turtle.tracer(0) #turns off all animation
#modules
import paddle
import ball
import score
import time

turtle.speed(0)
turtle.bgcolor('black')
turtle.hideturtle()
screen = turtle.Screen()

#inputs

try:
    x = turtle.numinput(title="Game Setup Width", prompt="Choose the width of the game: \n width: 660 * height: 325 - recommended")
    y = turtle.numinput(title="Game Setup Height", prompt="Enter the height of the game: \n width: 660 * height: 325 - recommended")
    
except:
    x = 660
    y = 325

#objects from classes
paddle_1 = paddle.Paddle(x, 0)

paddle_2 = paddle.Paddle(-x, 0)

ball = ball.Ball(x, y)

score = score.Score("blue", "red", x, y)

#functions
def draw_middle_line():
    """to draw a middle line"""
    turtle.setheading(90)
    turtle.setposition(0, -y)
    turtle.color('white')
    
    for i in range(int(y)+40//30):
        turtle.fd(30)
        turtle.penup()
        turtle.fd(30)
        turtle.pendown()

#draw middle section
draw_middle_line()

turtle.listen()
    
game_on = True
while game_on:
    time.sleep(ball.ball_speed)
    turtle.update() #updates the screen every time
    
    #paddle 1       
    if True:
        #controls
        screen.onkey(paddle_1.move_up, "Up")
        screen.onkey(paddle_1.move_down, "Down")

    #paddle 2
    if True:
        #controls
        screen.onkey(paddle_2.move_up, "w")
        screen.onkey(paddle_2.move_down, "s")
    
    ball.move_ball()
      
    ball.bounce_from_vertical_wall()
    
    #for ball bouncing on paddles
    if ball.distance(paddle_1.position()) < 55 and ball.xcor() > x-30:
        ball.bounce_paddles()
    elif ball.started >= 1:
        if ball.distance(paddle_2.position()) < 55 and ball.xcor() < -x+30:
            ball.bounce_paddles()
     
    #detects when player1 lost                 
    if ball.xcor() > x:
        ball.setx(-x+40)
        ball.reset_speed()
        score.win_player2()
    #detects when player2 lost
    if ball.xcor() < -x:
        ball.setx(x-42)
        ball.reset_speed()
        score.win_player1()
        
screen.exitonclick()