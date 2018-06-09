class weather:
    def __init__(self, weather_type):
        self.set_weather_details(weather_type)

    def set_weather_details(self, value):
        if value == 'sunny':
            self.crater_percent = -10
            self.vehicle = ['bike', 'tuktuk', 'car', ]
        elif value == 'rainy':
            self.crater_percent = 20
            self.vehicle = ['tuktuk', 'car', ]
        elif value == 'windy':
            self.crater_percent = 0
            self.vehicle = ['bike','car']

    def get_weather_details(self):
        return self.crater_percent, self.vehicle
