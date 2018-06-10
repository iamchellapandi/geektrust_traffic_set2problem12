class vehicle:
    def __init__(self, vehicle_name):
        self.set_vehicle_details(vehicle_name)

    def set_vehicle_details(self, value):
        if value == 'Bike':
            self.speed = 10
            self.crater_time = 2
            self.vehicle_rank = 1
        elif value == 'Tuktuk':
            self.speed = 12
            self.crater_time = 1
            self.vehicle_rank = 2
        elif value == 'Car':
            self.speed = 20
            self.crater_time = 3
            self.vehicle_rank = 3

    def get_vehicle_details(self):
        return self.speed, self.crater_time, self.vehicle_rank


if __name__ == '__main__':
    vc = vehicle('car')
    print (vc.get_vehicle_details())
