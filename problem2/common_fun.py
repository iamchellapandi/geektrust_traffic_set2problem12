import orbit
import vehicle
import weather
import re

def get_weather_info(in_weather):
    try:
        in_weather_info = re.search(r'^Weather\sis\s(\w+)', in_weather.strip()).group(1)
        out_weather_info = weather.weather(in_weather_info)
        weather_crater_percent, weather_vehicle_list = out_weather_info.get_weather_details()
    except:
        pass
    return weather_crater_percent, weather_vehicle_list

def get_orbit_info(orbit_str):
    local = orbit_str.strip().split()
    in_orbit_name, traffic_speed = local[0], int(local[-2])
    out_orbit_info  = orbit.orbit(in_orbit_name)
    orbit_distance,orbit_crater = out_orbit_info.get_orbit_details()
    return in_orbit_name,orbit_distance, orbit_crater, traffic_speed


def final_cal(orbit_name,crater_percent, vehicle_list, distance, craters, traffic_speed, result):
    if crater_percent < 0:
        actual_crater = craters - (craters*(abs(crater_percent))/100)
    elif crater_percent >= 0 :
        actual_crater = craters + ((craters*crater_percent)/100)

    
    for vc in vehicle_list:
        vc_obj = vehicle.vehicle(vc)
        vehicle_speed,crater_time,rank = vc_obj.get_vehicle_details()
        if vehicle_speed >= traffic_speed:
            speed = traffic_speed
        else:
            speed = vehicle_speed
        time = ((60/speed)*distance)+(actual_crater*crater_time)
        result.append([time, vc, orbit_name,rank])
    return result
