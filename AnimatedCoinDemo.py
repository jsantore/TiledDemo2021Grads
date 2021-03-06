import arcade
import pathlib
from typing import List

FRAME_HEIGHT = 512
FRAME_WIDTH = 512

class AnimatedSpriteWindow (arcade.Window):
    def __init__(self):
        super().__init__(600, 600, "Demo Animated Sprite")
        self.coin_sprite = None
        self.thing_list = None

    def setup(self):
        coin_path = pathlib.Path.cwd()/'Assets'/'Coin_Spin_Animation_A.png'
        self.coin_sprite = \
            arcade.AnimatedTimeBasedSprite(coin_path, 1, center_x=300, center_y=300)
        coin_frames: List[arcade.AnimationKeyframe] = []
        for row in range(4):
            for col in range(4):
                frame = \
                    arcade.AnimationKeyframe(col * row, 60, arcade.load_texture(str(coin_path),
                                                                                 x=col * FRAME_WIDTH,
                                                                                 y=row * FRAME_HEIGHT,
                                                                                 width=FRAME_WIDTH,
                                                                                 height=FRAME_HEIGHT))
                coin_frames.append(frame)
        self.coin_sprite.frames = coin_frames
        self.thing_list = arcade.SpriteList()
        self.thing_list.append(self.coin_sprite)

    def update(self, delta_time: float):
        self.coin_sprite.update_animation()

    def on_draw(self):
        arcade.start_render()
        self.thing_list.draw()

def main():
    game_window = AnimatedSpriteWindow()
    game_window.setup()
    arcade.run()

if __name__ == '__main__':
    main()