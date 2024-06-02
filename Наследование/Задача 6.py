class Transport:
    def __init__(self, name):
        self.name = name

    def move(self):
        pass

class WaterTransport(Transport):
    def __init__(self, name):
        super().__init__(name)

    def navigate(self):
        pass

class AirTransport(Transport):
    def __init__(self, name):
        super().__init__(name)

    def fly(self):
        pass

class Aviation(AirTransport):
    def __init__(self, name):
        super().__init__(name)

    def fly(self):
        print("Flying like an airplane")

class Airship(AirTransport):
    def __init__(self, name):
        super().__init__(name)

    def fly(self):
        print("Flying like an airship")

class HotAirBalloon(AirTransport):
    def __init__(self, name):
        super().__init__(name)

    def fly(self):
        print("Flying like a hot air balloon")

class LandTransport(Transport):
    def __init__(self, name):
        super().__init__(name)

    def drive(self):
        pass

class Railway(LandTransport):
    def __init__(self, name):
        super().__init__(name)

    def drive(self):
        print("Traveling by train")

class Automobile(LandTransport):
    def __init__(self, name):
        super().__init__(name)

    def drive(self):
        print("Driving a car")

class Bicycle(LandTransport):
    def __init__(self, name):
        super().__init__(name)

    def ride(self):
        print("Riding a bicycle")

class AnimalPowered(LandTransport):
    def __init__(self, name):
        super().__init__(name)

    def move(self):
        print("Being moved by animals")

class SpaceTransport(Transport):
    def __init__(self, name):
        super().__init__(name)

    def travel(self):
        pass

class Rocket(SpaceTransport):
    def __init__(self, name):
        super().__init__(name)

    def travel(self):
        print("Traveling by rocket")

class Shuttle(SpaceTransport):
    def __init__(self, name):
        super().__init__(name)

    def travel(self):
        print("Traveling by space shuttle")