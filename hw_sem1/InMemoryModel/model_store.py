
from zope.interface import implementer
from hw_sem1.ModelElements.camera import Camera
from hw_sem1.ModelElements.flash import Flash
from hw_sem1.ModelElements.scene import Scene
from hw_sem1.ModelElements.poligonal_model import PoligonalModel
from hw_sem1.InMemoryModel.i_model_changed_observer import IModelChangedObserver
from hw_sem1.InMemoryModel.i_model_changer import IModelChanger


@implementer(IModelChanger)
class ModelStore:
    def __init__(self, interface: IModelChangedObserver=None):
        self.models: list[PoligonalModel] = [PoligonalModel()]
        self.scenes: list[Scene] = [Scene(id=None, model=None, camera=None)]
        self.flashes: list[Flash] = [Flash(location=None, angle=None, color=None, power=None)]
        self.cameras: list[Camera] = [Camera(location=None, angle=None)]
        self._change_observers: list[IModelChangedObserver] = [interface]

    def get_scena(self, id: int) -> Scene:
        pass

    def notify_change(changer: IModelChanger):
        pass