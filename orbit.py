class orbit:
    def __init__(self,orbit_name):
        self.set_orbit_details(orbit_name)

    def set_orbit_details(self,value):
        if value == 'Orbit1':
            self.orbit_distance = 18
            self.orbit_crater = 20
        elif value == 'Orbit2':
            self.orbit_distance = 20
            self.orbit_crater = 10
        elif value == 'Orbit3':
            self.orbit_distance = 30
            self.orbit_crater = 15
        elif value == 'Orbit4':
            self.orbit_distance = 15
            self.orbit_crater = 18
    def get_orbit_details(self):
        return self.orbit_distance,self.orbit_crater



if __name__ == '__main__':
    ob = orbit('orbit1')
    print(ob.get_orbit_details())
