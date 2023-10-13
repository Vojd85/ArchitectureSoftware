from some_classes import Type
from poligonal_model import PoligonalModel
from camera import Camera
from flash import Flash


class Scene:
    def __init__(self, id: int, model: PoligonalModel, camera: Camera, flash: Flash=None):
        self.id = id
        self.models = [model]
        self.cameras = [camera]
        self.flashes = [flash]

    def method_1(type: Type) -> Type:
        pass

    def method_1(type_1: Type, type_2: Type) -> Type:
        pass