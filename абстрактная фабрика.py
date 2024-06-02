from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def drive(self):
        pass

class ElectricCar(Car):
    def drive(self):
        print("Driving an electric car.")

class PetrolCar(Car):
    def drive(self):
        print("Driving a petrol car.")

class HybridCar(Car):
    def drive(self):
        print("Driving a hybrid car.")

class CarFactory(ABC):
    @abstractmethod
    def produce_car(self):
        pass

class ElectricCarFactory(CarFactory):
    def produce_car(self):
        return ElectricCar()

class PetrolCarFactory(CarFactory):
    def produce_car(self):
        return PetrolCar()

class HybridCarFactory(CarFactory):
    def produce_car(self):
        return HybridCar()

electric_factory = ElectricCarFactory()
petrol_factory = PetrolCarFactory()
hybrid_factory = HybridCarFactory()

electric_car = electric_factory.produce_car()
petrol_car = petrol_factory.produce_car()
hybrid_car = hybrid_factory.produce_car()

electric_car.drive()
# Вывод: Driving an electric car.
petrol_car.drive()
# Вывод: Driving a petrol car.
hybrid_car.drive()
# Вывод: Driving a hybrid car.