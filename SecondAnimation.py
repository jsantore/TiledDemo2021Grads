import arcade
import pathlib

class AnimatedSpriteWindow2(arcade.Window):
    def __init__(self):
        super().__init__(700, 700, "Time Based Animation Demo")
        self.raccoon: arcade.AnimatedTimeBasedSprite = None
        self.thing_list: arcade.SpriteList = None

    def setup(self):
        path = pathlib.Path.cwd() / 'Assets' / 'raccoon-walk'
        self.raccoon = \
            arcade.AnimatedTimeBasedSprite(path/'walk0001.png' ,0.75, center_x=300, center_y=300)
        self.thing_list = arcade.SpriteList()
        all_files = path.glob('*.png')  # return a generator with all the qualified paths to all png files in dir
        textures = []
        count = 0
        for file_path in all_files:
            count +=1
            frame = arcade.AnimationKeyframe( count, 10, arcade.load_texture(str(file_path)))  # we want the whole image
            textures.append(frame)
            print(textures)  # for debugging purposes only
            self.raccoon.frames = textures
        self.thing_list.append(self.raccoon)

    def update(self, delta_time: float):
        self.raccoon.update_animation()

    def on_draw(self):
        arcade.start_render()
        self.thing_list.draw()


def main():
    window = AnimatedSpriteWindow2()
    window.setup()
    arcade.run()

if __name__ == '__main__':
    main()