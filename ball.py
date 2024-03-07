from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_shift = 20
        self.y_shift = 20
        self.shape("circle")
        self.penup()
        self.color("red")
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_shift
        new_y = self.ycor() + self.y_shift
        self.goto(new_x, new_y)

        # detect collision with the wall
        if self.ycor() >= 280 or self.ycor() <= -280:
            self.wall_bounce()

    def wall_bounce(self):
        self.y_shift *= -1

    def paddle_bounce(self):
        self.x_shift *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.x_shift *= -1
        self.move_speed = 0.1
