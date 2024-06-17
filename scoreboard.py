import turtle as t

SCORE_FONT = ("Small Fonts", 42, "normal")


class Scoreboard(t.Turtle):

    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.score_list = []
        self.scoreboard_left = None
        self.scoreboard_right = None
        self.create_scoreboard()
        self.update_scoreboard()

    def create_scoreboard(self):
        for scoreboard in range(2):
            scoreboard = t.Turtle()
            scoreboard.speed("fastest")
            scoreboard.hideturtle()
            scoreboard.color("white")
            scoreboard.penup()
            self.score_list.append(scoreboard)
        self.scoreboard_left = self.score_list[0]
        self.scoreboard_right = self.score_list[1]
        self.scoreboard_left.goto(-100, 320)
        self.scoreboard_right.goto(100, 320)

    def update_scoreboard(self):
        self.scoreboard_left.clear()
        self.scoreboard_right.clear()
        self.scoreboard_left.write(f"{self.score_left}", align="left", font=SCORE_FONT)
        self.scoreboard_right.write(f"{self.score_right}", align="right", font=SCORE_FONT)

    def increase_score_left(self):
        self.score_left += 1
        self.update_scoreboard()

    def increase_score_right(self):
        self.score_right += 1
        self.update_scoreboard()

    def is_game_over(self):
        """Checks if the game is over and displays the winner"""
        if self.score_left > self.score_right and self.score_left >= 10:
            return True
        elif self.score_right > self.score_left and self.score_right >= 10:
            return True
        else:
            return False
