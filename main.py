import arcade
import time
# TODO: fix sound, find a way to keep it from playing over itself

# global variables
screen_width = 600
screen_height = 600
game_title = "temp"


class MainGame(arcade.Window):
    # constructors for both the derived and the parent classes
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    # declaring the instance variables ---> maybe these are considered class variables?
    _mouse_visible = False
    left_choice_pressed = False
    right_choice_pressed = False

    current_background = None
    menu_background = None
    level_background_list = None

    mouse_cursor_sprite = None
    play_button = None

    current_sound = None
    menu_sound = None

    tick = None
    timer = None

    """all variable/sprites will be setup in the setup function"""
    def setup(self):
        self.mouse_cursor_sprite = arcade.Sprite("game_assets/Cursor1.png", center_x=300, center_y=300)
        self.play_button = arcade.Sprite("game_assets/play_button.png", center_x=300, center_y=500, scale=0.3)

        self.menu_background = arcade.load_texture("game_backgrounds/menu_background_woods.jpg", width=600, height=600)
        self.current_background = self.menu_background

        self.menu_sound = arcade.load_sound("game_sounds/menu_sound_woods_ambiance.mp3")
        self.current_sound = self.menu_sound

        self.tick = 2

    """all drawing of sprites and the game screen will be done in the on_draw function"""
    def on_draw(self):
        arcade.start_render()

        if self.current_background == self.menu_background:
            arcade.draw_texture_rectangle(screen_width / 2, screen_height/2, screen_width, screen_height,
                                          self.current_background)
            self.play_button.draw()
            if self.tick > 1:
                arcade.play_sound(self.current_sound)
                self.tick -= 1

        self.mouse_cursor_sprite.draw()

    """game logic will be in the update function"""
    def update(self, delta_time):
        pass

    """mouse cursor sprite logic will be in the on_mouse_motion function"""

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.mouse_cursor_sprite.center_x = x + 5.5
        self.mouse_cursor_sprite.center_y = y - 7.5

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
    arcade.run()


if __name__ == "__main__":
    main()
