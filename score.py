import turtle

class Score(turtle.Turtle):
    def __init__(self, color_p1, color_p2, x, y):
        super().__init__()
        self.speed(0)
        self.penup()
        self.hideturtle()
        self.x = x
        self.y = y
        self.score_p1 = 0     
        self.score_p2 = 0
        self.color1 = color_p1
        self.color2 = color_p2
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.color(self.color1)
        self.setposition(self.x*0.5, self.y-80)
        self.write(f"{self.score_p1}", align='center', font=("Courier", 40, "normal"))
        self.color(self.color2)
        self.setposition(-self.x*0.5, self.y-80)
        self.write(f"{self.score_p2}", align='center', font=("Courier", 40, "normal"))
        
        #adds 1 point to player 1
    def win_player1(self):
        self.score_p1 += 1
        self.update_score()
        #adds 1 point to player 2
    def win_player2(self):
        self.score_p2 += 1
        self.update_score()
        