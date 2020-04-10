import arcade

# global variables
screen_width = 600
screen_height = 600
game_title = "temp"

class MainGame(arcade.Window):
    def __init__(self, width, height, title)
        super().__init__(width, height, title)


    def setup(self):
        pass

    def on_draw(self):
        pass

    def update(self, delta_time):
        pass

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float, button):
        pass

    def on_mouse_press(self, x: float, y: float, button):
        pass

    def on_mouse_release(self, x: float, y: float, button):
        pass

def main():
    game = MainGame(screen_width, screen_height, game_title)

if __name__ == "__main__":
    main()