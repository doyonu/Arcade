import arcade


class MyGame(arcade.Window):
   def __init__(self, width, height, title):
       super().__init__(width, height, title)

    def setup(self):
        arcade.set_background_color(arcade.color.WHITE)

def main():

    window = MyGame(640, 480, "Drawing Example")

    arcade.run()

main()

def on_draw(self):

    arcade.start_render()


    arcade.draw_circle_filled(10, 10, 20, (225, 54, 34))