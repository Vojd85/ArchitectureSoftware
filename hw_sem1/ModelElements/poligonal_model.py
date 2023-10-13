from poligon import Poligon
from texture import Texture


class PoligonalModel:
    def __init__(self, texture: Texture=None):
        self.textures: list[Texture] = [texture]
        self.poligons: list[Poligon] = [Poligon()]