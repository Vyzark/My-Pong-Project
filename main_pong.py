import time
import turtle as t

import ball
import paddle
import scoreboard

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

s = t.Screen()


class Main:
    def __init__(self):
        ### Screen setup ###
        self.s = t.Screen()
        self.s.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.s.bgcolor("black")
        self.s.title("Pong Game")
        self.s.tracer(0)
        ### Paddle setup ###
        self.paddle_object = paddle.Paddle(screen_width=SCREEN_WIDTH, screen_height=SCREEN_HEIGHT)
        ### Ball setup ###
        self.ball_object = ball.Ball(SCREEN_HEIGHT)
        ### Scoreboard setup ###
        self.scoreboard = scoreboard.Scoreboard()
        self.scoreboard.hideturtle()

    def reset_padddles(self):
        """Resets the paddles to the center of the screen"""
        self.paddle_object.left_paddle.goto(-450, 0)
        self.paddle_object.right_paddle.goto(450, 0)

    def reset_ball(self):
        """Resets the ball to the center of the screen and changes the direction"""
        self.ball_object.ball.goto(0, 0)
        self.ball_object.x_move *= -1

    @staticmethod
    def left_player_wins():
        """Displays the left player wins message"""
        score_writing = t.Turtle()
        score_writing.hideturtle()
        score_writing.color("white")
        score_writing.write("Left Player Wins!", align="center", font=("Small Fonts", 42, "normal"))

    @staticmethod
    def right_player_wins():
        """Displays the right player wins message"""
        score_writing = t.Turtle()
        score_writing.hideturtle()
        score_writing.color("white")
        score_writing.write("Right Player Wins!", align="center", font=("Small Fonts", 42, "normal"))


    def main(self):
        ragnarok = False
        speed = 0.06
        while not ragnarok:
            if self.scoreboard.is_game_over():
                if self.scoreboard.score_left > self.scoreboard.score_right:  # If left player wins
                    self.ball_object.ball.hideturtle()
                    self.left_player_wins()
                elif self.scoreboard.score_right > self.scoreboard.score_left:  # If right player wins
                    self.ball_object.ball.hideturtle()
                    self.right_player_wins()
                ragnarok = True
            self.paddle_object.restrict_movement()  # Needs to be called at the start of the loop
            self.ball_object.bounce_wall()
            if self.ball_object.bounce_paddle(self.paddle_object.left_paddle, self.paddle_object.right_paddle):
                speed *= 0.75
            if self.ball_object.ball.xcor() >= 490:  # Score for left player
                self.scoreboard.increase_score_left()
                self.reset_ball()
                self.reset_padddles()
                speed = 0.06
            elif self.ball_object.ball.xcor() <= -490:  # Score for right player
                self.scoreboard.increase_score_right()
                self.reset_ball()
                self.reset_padddles()
                speed = 0.06
            self.ball_object.move()
            self.s.update()
            time.sleep(speed)

            self.s.onkeypress(fun=self.s.exitonclick, key="Escape")

        s.exitonclick()


Main().main()
