#ulysse doyon

import arcade
import random

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700

#classe objet balle
class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.change_x = 0
        self.change_y = 0
        self.size = 0
        self.color = None

#info sur la balle
def make_ball(x,y):
    ball = Ball(x,y)
    ball.size = random.randint(15,30)
    ball.x = x
    ball.y = y
    ball.change_x = random.randint(-7,7)
    ball.change_y = random.randint(-7,7)
    ball.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    return ball

#classe objet rectangle
class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.angle = 0
        self.change_x = 0
        self.change_y = 0
        self.color = None

#info sur le rectangle
def make_rectangle(x,y):
    rectangle = Rectangle(x,y)
    rectangle.x = x
    rectangle.y = y
    rectangle.width = random.randint(15,30)
    rectangle.height = random.randint(30,60)
    rectangle.angle = 90
    rectangle.change_x = random.randint(-7,7)
    rectangle.change_y = random.randint(-7,7)
    rectangle.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    return rectangle

#classe window
class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        self.ball_list = []
        #ball = make_ball()
        #self.ball_list.append(ball)
        self.rectangle_list = []
        #rectangle = make_rectangle()
        #self.rectangle_list.append(rectangle)
#fond d'écran
    def setup(self):
        arcade.set_background_color(arcade.color.BLACK)
        pass
#faire les objets
    def on_draw(self):
        arcade.start_render()
        for ball in self.ball_list:
            arcade.draw_circle_filled(ball.x, ball.y, ball.size, ball.color)
            pass
        for rectangle in self.rectangle_list:
            arcade.draw_rectangle_filled(rectangle.x, rectangle.y, rectangle.width, rectangle.height, rectangle.color, rectangle.angle)
            pass
#changement de direction "mur"
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
# faire les objets sur la souris
    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            ball = make_ball(x,y)
            self.ball_list.append(ball)
        if button == arcade.MOUSE_BUTTON_RIGHT:
            rectangle = make_rectangle(x,y)
            self.rectangle_list.append(rectangle)

def main():
    my_game = MyGame()
    my_game.setup()
    arcade.run()
main()