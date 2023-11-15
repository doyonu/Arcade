import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

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
    ball.color = arcade.color.CRIMSON
    return ball

class Rectangle:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.angle = 0
        self.change_x = 0
        self.change_y = 0
        self.color = None
def make_rectangle():
    rectangle = Rectangle()

    rectangle.x = 400
    rectangle.y = 400
    rectangle.width = 10
    rectangle.height = 20
    rectangle.angle = 0
    rectangle.change_x = 5
    rectangle.change_y = 5
    rectangle.color = arcade.color.APPLE_GREEN
    return rectangle

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        self.ball_list = []
        ball = make_ball()
        self.ball_list.append(ball)

        self.rectangle_list = []
        rectangle = make_rectangle()
        self.rectangle_list.append(rectangle)

    def setup(self):
        arcade.set_background_color((172, 229, 238))
        pass

    def on_draw(self):
        arcade.start_render()
        for ball in self.ball_list:
            arcade.draw_circle_filled(ball.x, ball.y, ball.size, ball.color)
            pass
        for rectangle in self.rectangle_list:
            arcade.draw_rectangle_filled(rectangle.x, rectangle.y, rectangle.width, rectangle.height, rectangle.color, rectangle.angle)
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

        for rectangle in self.rectangle_list:
            rectangle.x += rectangle.change_x
            rectangle.y += rectangle.change_y

            if rectangle.x < rectangle.width:
                rectangle.change_x *= -1

            if rectangle.y < rectangle.height:
                rectangle.change_y *= -1

            if rectangle.x > SCREEN_WIDTH - rectangle.width:
                rectangle.change_x *= -1

            if rectangle.y > SCREEN_HEIGHT - rectangle.height:
                rectangle.change_y *= -1

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            ball = make_ball()
            self.ball_list.append(ball)
        if button == arcade.MOUSE_BUTTON_RIGHT:
            rectangle = make_rectangle()
            self.rectangle_list.append(rectangle)


def main():
    my_game = MyGame()
    my_game.setup()
    arcade.run()

main()
