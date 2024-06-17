import turtle as t

STEP_SIZE = 40


class Paddle(t.Turtle):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.new_paddle = None
        self.x_margin = (screen_width / 2) - 50
        self.y_margin = (screen_height / 2) - 60
        self.paddles = []
        self.resizemode("user")
        self.s = t.Screen()
        self.create_paddles()
        self.right_paddle = self.paddles[0]
        self.left_paddle = self.paddles[1]
        self.move_keys()

    def create_paddles(self):  # TODO: Fix the paddles moving on the side
        """
        Creates the new_paddle
        """
        for _ in range(2):
            self.new_paddle = t.Turtle(shape="square")
            self.new_paddle.penup()
            self.new_paddle.speed("fastest")
            self.new_paddle.color("white")
            self.new_paddle.shapesize(stretch_wid=5, stretch_len=1)
            self.new_paddle.goto(self.x_margin, 0)
            self.paddles.append(self.new_paddle)
            self.x_margin *= -1

    def move_up_one(self):
        """
        Moves the right paddle up
        """
        self.right_paddle.goto(self.right_paddle.xcor(),
                               self.right_paddle.ycor() + STEP_SIZE)

    def move_down_one(self):
        """
        Moves the right paddle down
        """
        self.right_paddle.goto(self.right_paddle.xcor(),
                               self.right_paddle.ycor() - STEP_SIZE)

    def move_up_two(self):
        """
        Moves the left paddle up
        """
        self.left_paddle.goto(self.left_paddle.xcor(),
                              self.left_paddle.ycor() + STEP_SIZE)

    def move_down_two(self):
        """
        Moves the left paddle down
        """
        self.left_paddle.goto(self.left_paddle.xcor(),
                              self.left_paddle.ycor() - STEP_SIZE)

    def restrict_movement(self):
        """
        Restricts the movement of the paddles within the screen
        """
        for paddle in self.paddles:
            if paddle.ycor() > self.y_margin:
                paddle.goto(paddle.xcor(), self.y_margin)
            elif paddle.ycor() < -self.y_margin:
                paddle.goto(paddle.xcor(), -self.y_margin)

    def move_keys(self):
        """
        Controls the paddles with the keyboard
        """
        self.s.listen()
        # Player 1 (right paddle)
        self.s.onkeypress(self.move_up_one, "Up")
        self.s.onkeypress(self.move_down_one, "Down")
        # Player 2 (left paddle)
        self.s.onkeypress(self.move_up_two, "w")
        self.s.onkeypress(self.move_down_two, "s")
