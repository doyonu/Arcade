import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = []

class Ball:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0
        self.size = 0
        self.color = None


def make_ball():

    ball = Ball()

    ball.size = 20

    ball.x = 20
    ball.y = 20

    ball.change_x = 5
    ball.change_y = 5

    ball.color = arcade.color.LIGHT_CRIMSON

    return ball

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        self.ball_list = []
        ball = make_ball()
        self.ball_list.append(ball)

    def setup(self):
        arcade.set_background_color((172, 229, 238))
        pass

    def on_draw(self):
        arcade.start_render()
        for ball in self.ball_list:
            arcade.draw_circle_filled(ball.x, ball.y, ball.size, arcade.color.CRIMSON)
            pass

    def on_update(self, delta_time):

        for ball in self.ball_list:
            ball.x += ball.change_x
            ball.y += ball.change_y

            if ball.x < ball.size:
                ball.change_x *= -1

            if ball.y < ball.size:
                ball.change_y *= -1

            if ball.x > SCREEN_WIDTH - ball.size:
                ball.change_x *= -1

            if ball.y > SCREEN_HEIGHT - ball.size:
                ball.change_y *= -1


def main():
    my_game = MyGame()
    my_game.setup()
    arcade.run()

main()
