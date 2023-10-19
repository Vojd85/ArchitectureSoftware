from abc import ABC, abstractmethod


class Engine(ABC):
    @abstractmethod
    def start_engine():
        pass

    def stop_engine():
        pass


class DiezelEngine(Engine):
    def start_engine(self):
        print('Врууум! И тут запахло соляркой...')

    def stop_engine(self):
        print('Двигатель выключится сам через 2 минуты')

class PetrolEngine(Engine):
    def start_engine(self):
        print('Врууум!')

    def stop_engine(self):
        print('Двигатель остановлен')


class Car:
    def __init__(self, model: str, engine: Engine, horsepower: int=None):
        self.model = model
        self._engine = engine
        self.hp = horsepower
        if isinstance(engine, DiezelEngine):
            self.eng_type = 'дизельный'
        elif isinstance(engine, PetrolEngine):
            self.eng_type = 'бензиновый'

    def __str__(self):
        return f"{self.model} тип двигателя: {self.eng_type} HP: {self.hp}"
    
    @property
    def engine(self):
        return self._engine
    

if __name__ == '__main__':
    benzin_car = Car('Лада Брусника', PetrolEngine(), 65)
    print(benzin_car)
    benzin_car.engine.start_engine()
    benzin_car.engine.stop_engine()

    diezel_car = Car('Ford Tranzit', DiezelEngine(), 99)
    print(diezel_car)
    diezel_car.engine.start_engine()
    diezel_car.engine.stop_engine()