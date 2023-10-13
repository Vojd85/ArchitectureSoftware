from some_classes import Point3D, Angle3D, Color, Float


class Flash:
    def __init__(self, location: Point3D, angle: Angle3D, 
                 color: Color, power: Float):
        self.location = location
        self.angle = angle
        self.color = color
        self.power = power

    def rotate(self, angle: Angle3D):
        pass

    def move(self, point: Point3D):
        pass