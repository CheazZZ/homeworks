import abc


class TransportVehicle(abc.ABC):

    @abc.abstractmethod
    def ride(self):
        pass

    @abc.abstractmethod
    def stop(self):
        pass

    @abc.abstractmethod
    def refuel(self):
        pass

    @abc.abstractmethod
    def set_the_alarm(self):
        pass

    @abc.abstractmethod
    def turn_on_wipers(self):
        pass


class TransportVehicleBase(TransportVehicle):

    def __init__(self, name, color, capacity, power, transmission):
        self.name = name
        self.color = color
        self.capacity = capacity
        self.power = power
        self.transmission = transmission

    def ride(self):
        print('Riding now')

    def stop(self):
        print('Brake')

    def refuel(self):
        print('Refueling')

    def set_the_alarm(self):
        print('Alarm turns on')

    def turn_on_wipers(self):
        print('Wipers are active')

    def get_vehicle_info(self):
        template: str = (f'\nMark: {self.name}'
                         f'\nColor: {self.color}'
                         f'\nCapacity: {self.capacity}'
                         f'\nPower: {self.power}'
                         f'\nTransmission: {self.transmission}')
        print(template)


class Car(TransportVehicleBase):

    def __init__(self, name, color, capacity, power, transmission):
        super().__init__(name, color, capacity, power, transmission)

    def ride(self):
        super().ride()
        print('Car is on the road :o')


class Bicycle(TransportVehicleBase):

    def __init__(self, name, color, capacity, power, transmission):
        super().__init__(name, color, capacity, power, transmission)


class Bus(TransportVehicleBase):

    def __init__(self, name, color, capacity, power, transmission):
        super().__init__(name, color, capacity, power, transmission)


volkswagen = Car('Volkswagen Tiguan', 'White', '1834см3', '167hp', 'robot')
stels = Bicycle('Stels', 'Black', 'Blank', 'Blank', 'mechanics')
isuzu = Bus('ISUZU', 'Red', '1023см3', '108hp', 'automat')

volkswagen.ride()
