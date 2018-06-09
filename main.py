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

        

if __name__ == '__main__':
    result_list = []
    #print 'Enter the weather info:'
    in_weather = raw_input()
    #in_weather = 'Weather is Windy'
    weather_crater_percent, weather_vehicle_list = get_weather_info(in_weather)
    #print 'enter orb 1 deatils:'
    in_orb_1 = raw_input()
    #in_orb_1 = 'Orbit1 traffic speed is 14 megamiles/hour'
    orbit_name,orbit_distance, orbit_crater, traffic_speed = get_orbit_info(in_orb_1)
    result = final_cal(orbit_name,weather_crater_percent, weather_vehicle_list,orbit_distance, orbit_crater, traffic_speed, result_list)
    #print 'enter orb 2 deatils:'
    in_orb_2 = raw_input()
    orbit_name,orbit_distance, orbit_crater, traffic_speed = get_orbit_info(in_orb_2)
    result= final_cal(orbit_name,weather_crater_percent, weather_vehicle_list,orbit_distance, orbit_crater, traffic_speed, result_list)
    vc_un_sort = sorted(result, key=lambda result: result[3], reverse=False)
    sorted_result = sorted(vc_un_sort, key=lambda vc_un_sort: vc_un_sort[0],reverse = False)
    print 'Vehicle '+sorted_result[0][1]+' on '+sorted_result[0][2]
