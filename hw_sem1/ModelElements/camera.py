from some_classes import Point3D, Angle3D


class Camera:
    def __init__(self, location: Point3D, angle: Angle3D):
        self.location = location
        self.angle = angle

    def rotate(self, angle: Angle3D):
        pass

    def move(self, point: Point3D):
        pass