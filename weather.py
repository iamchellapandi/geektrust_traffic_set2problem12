class weather:
    def __init__(self, weather_type):
        self.set_weather_details(weather_type)

    def set_weather_details(self, value):
        if value == 'Sunny':
            self.crater_percent = -10
            self.vehicle = ['Bike', 'Tuktuk', 'Car', ]
        elif value == 'Rainy':
            self.crater_percent = 20
            self.vehicle = ['Tuktuk', 'Car', ]
        elif value == 'Windy':
            self.crater_percent = 0
            self.vehicle = ['Bike','Car']

    def get_weather_details(self):
        return self.crater_percent, self.vehicle
