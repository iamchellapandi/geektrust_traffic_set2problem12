import common_fun


if __name__ == '__main__':
    result_list = []
    in_weather = raw_input()
    weather_crater_percent, weather_vehicle_list = common_fun.get_weather_info(
        in_weather)
    in_orb_1 = raw_input()
    orbit_name, orbit_distance, orbit_crater, traffic_speed = common_fun.get_orbit_info(in_orb_1)
    result = common_fun.final_cal(orbit_name, weather_crater_percent, weather_vehicle_list, orbit_distance, orbit_crater, traffic_speed, result_list)
    in_orb_2 = raw_input()
    orbit_name, orbit_distance, orbit_crater, traffic_speed = common_fun.get_orbit_info(in_orb_2)
    result = common_fun.final_cal(orbit_name, weather_crater_percent, weather_vehicle_list,orbit_distance, orbit_crater, traffic_speed, result_list)
    vc_un_sort = sorted(result, key=lambda result: result[3], reverse=False)
    sorted_result = sorted(vc_un_sort, key=lambda vc_un_sort: vc_un_sort[0],reverse = False)
    print 'Vehicle '+sorted_result[0][1]+' on '+sorted_result[0][2]
