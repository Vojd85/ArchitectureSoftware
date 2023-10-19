from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area():
        pass

    @abstractmethod
    def perimeter():
        pass


class Shape_3D(ABC):
    @abstractmethod
    def volume():
        pass


class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.a_side = length
        self.b_side = width
    
    def area(self):
        return self.a_side * self.b_side
    
    def perimeter(self):
        return (self.a_side + self.b_side) * 2
    

class Cube(Shape_3D):
    def __init__(self, length: float, width: float, height: float):
        self.a_side = length
        self.b_side = width
        self.c_side = height

    def volume(self):
        return self.a_side * self.b_side * self.c_side
    

if __name__ == '__main__':
    rect = Rectangle(2.3, 5)
    cube = Cube(4, 4, 4)
    print(f'{rect.area()}\n{rect.perimeter()}\n{cube.volume()}')