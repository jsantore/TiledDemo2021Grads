import arcade
import pathlib


class TiledWindow (arcade.Window):
    def __init__(self):
        super().__init__(960, 960, "Initial Tiled Map Super Simple Example")
        self.map_location = pathlib.Path.cwd()/'Assets'/'sampleMap2.json'
        self.mapscene = None

    def setup(self):
        sample__map = arcade.tilemap.load_tilemap(self.map_location)
        self.mapscene = arcade.Scene.from_tilemap(sample__map)

    def on_draw(self):
        arcade.start_render()
        self.mapscene.draw()