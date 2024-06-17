import turtle as t


class Ball(t.Turtle):
    def __init__(self, height):
        super().__init__()
        self.ball = None
        self.y_margin = (height / 2) - 30
        self.create_ball()
        self.x_move = 10
        self.y_move = 10

    def create_ball(self):
        """Creates the ball at the center of the screen"""
        self.ball = t.Turtle(shape="circle")
        self.ball.penup()
        self.ball.speed("fastest")
        self.ball.color("white")
        self.ball.goto(0, 0)

    def move(self):
        """Moves the ball on x and y-axis"""
        self.ball.goto(self.ball.xcor() + self.x_move, self.ball.ycor() + self.y_move)

    def bounce_wall(self):
        """Detects collision with the top and bottom and bounces back by changing the y_move value"""
        if self.ball.ycor() > self.y_margin or self.ball.ycor() < -self.y_margin:
            self.y_move *= -1

    def bounce_paddle(self, left_paddle, right_paddle):
        """Detects collision with the paddle and bounces back by changing the x_move value"""
        if (self.ball.distance(right_paddle) < 50 and self.ball.xcor() >= 430 or
                self.ball.distance(left_paddle) < 50 and self.ball.xcor() <= -430):
            self.x_move *= -1
            return True
