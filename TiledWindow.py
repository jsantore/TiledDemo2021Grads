import arcade
import pathlib


class TiledWindow (arcade.Window):
    def __init__(self):
        super().__init__(960, 960, "Initial Tiled Map Super Simple Example")
        self.map_location = pathlib.Path.cwd()/'Assets'/'GradMap.json'
        self.mapscene = None
        self.player = None
        self.wall_layer = None
        self.player_list = None
        self.collision_engine = None
        self.move_speed = 3

    def setup(self):
        sample_map = arcade.tilemap.load_tilemap(self.map_location)
        self.mapscene = arcade.Scene.from_tilemap(sample_map)
        player_image_file = pathlib.Path.cwd()/'Assets'/'orc2.png'
        self.player = arcade.Sprite(player_image_file)
        self.player.center_x = 96  # in the middle of the second tile
        self.player.center_y = 224  # middle of the forth tile up
        self.wall_layer = sample_map.sprite_lists['WallLayer']
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player)
        self.collision_engine = arcade.PhysicsEngineSimple(self.player, self.wall_layer)

    def on_draw(self):
        arcade.start_render()
        self.mapscene.draw()
        self.player_list.draw()

    def on_update(self, delta_time: float):
        self.collision_engine.update()

    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.UP or key == arcade.key.W:
            self.player.change_y = self.move_speed
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player.change_y = -self.move_speed
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player.change_x = -self.move_speed
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player.change_x = self.move_speed

    def on_key_release(self, key: int, modifiers: int):
        if self.player.change_y > 0 and (key == arcade.key.UP or key == arcade.key.W):
            self.player.change_y = 0
        elif self.player.change_y < 0 and (key == arcade.key.DOWN or key == arcade.key.S):
            self.player.change_y = 0
        elif self.player.change_x < 0 and (key == arcade.key.LEFT or key == arcade.key.A):
            self.player.change_x = 0
        elif self.player.change_x > 0 and (key == arcade.key.RIGHT or key == arcade.key.D):
            self.player.change_x = 0