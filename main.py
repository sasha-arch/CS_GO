import arcade
from time import sleep
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
vector = 0
a = str('x')

def load_texture_pair(filename):
    """
    Load a texture pair, with the second being a mirror image.
    """
    return [
        arcade.load_texture(filename),
        arcade.load_texture(filename, flipped_horizontally=True),
    ]

class MyGame(arcade.Window):
    """ Main application class. """
    def __init__(self, width, height):
        super() .__init__(width, height, title="CS:GO")
        self.background = None
        self.texturaTer = None
    def setup(self):
        # Set up your game here
        self.background = arcade.load_texture('background.png', width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.coinlist = arcade.SpriteList()
        self.coinsprite = arcade.Sprite('new_terrorist.png', 0.08)
        self.coinsprite.center_x = 0
        self.coinsprite.center_y = (260/600) * SCREEN_HEIGHT
        texture = arcade.load_texture("new_terrorist.png")
        self.coinsprite.texture_list = []
        self.coinsprite.texture_list.append(texture)
        texture = arcade.load_texture('new_terrorist!.png')
        self.coinsprite.texture_list.append(texture)
        self.coinlist.append(self.coinsprite)
        self.alhlist = arcade.SpriteList()
        self.alhsprite = arcade.Sprite('new_alh.png', 1)
        self.alhsprite.center_x = (34/800)*SCREEN_WIDTH
        self.alhsprite.center_y = (414/600)*SCREEN_HEIGHT
        self.alhlist.append(self.alhsprite)
        self.scope_list = arcade.SpriteList()
        self.scope_sprite = arcade.Sprite('best_scope.png', 0.65)
        self.scope_list.append(self.scope_sprite)

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH ,SCREEN_HEIGHT , self.background)
        self.coinlist.draw()
        self.alhlist.draw()
        self.scope_sprite.draw()

        # Your drawing code goes here
    def spawnTer(self):
        self.coinlist.append(self.coinsprite)
        self.coinsprite.center_x = 0
        self.coinsprite.center_y = (260/600) * SCREEN_HEIGHT
        self.coinlist.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        self.scope_sprite.center_x = x
        self.scope_sprite.center_y = y

    def on_mouse_press(self, x, y, button, key_modifiers):
        if button == 1:
            if (x - self.coinsprite.center_x)**2 + (y - self.coinsprite.center_y)**2 <= 50.16**2:
                self.coinsprite.remove_from_sprite_lists()
                self.spawnTer()


    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        global vector
        if vector == 0:
            self.coinsprite.center_x += 1
        else:
            self.coinsprite.center_x -= 1

        if self.coinsprite.center_x >= 0.4625 * SCREEN_WIDTH:
            vector = 1
            self.coinsprite.texture = self.coinsprite.texture_list[1]
        elif self.coinsprite.center_x <= 1:
            vector = 0
            self.coinsprite.texture = self.coinsprite.texture_list[0]





def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()

