import arcade

# global variables
screen_width = 600
screen_height = 600
game_title = "temp"

class MainGame(arcade.Window):
    # constructors for both the derived and the parent classes
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    # declaring the instance variables ---> maybe these are considered class variables?
    left_choice_pressed = False
    right_choice_pressed = False

    level_background_list = None

    mouse_cursor_sprite = None

    """all variable/sprites will be setup in the setup function"""
    def setup(self):
        self.mouse_cursor_sprite = arcade.Sprite("game_assets/Cursor1.png", center_x=300, center_y=300)


    """all drawing of sprites and the game screen will be done in the on_draw function"""
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.RED)
        self.mouse_cursor_sprite.draw()

    """game logic will be in the update function"""
    def update(self, delta_time):
        pass

    """mouse cursor sprite logic will be in the on_mouse_motion function"""
    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        pass

    """all logic surrounding button presses will be in the on_mouse_press function"""
    def on_mouse_press(self, x: float, y: float, button):
        pass

    """button_pressed boolean variables will be reset to False in the on_mouse_release function"""
    def on_mouse_release(self, x: float, y: float, button):
        pass

"""main function"""
def main():
    game = MainGame(screen_width, screen_height, game_title)
    game.setup()
    game.on_draw()
    arcade.run()

if __name__ == "__main__":
    main()