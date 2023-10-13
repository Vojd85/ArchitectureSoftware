import zope.interface


class IModelChangedObserver(zope.interface.Interface):
    def apply_update_model():
        pass