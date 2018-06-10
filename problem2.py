import common_fun

def mission_possible(result_list):
    route_result = []
    for li in result_list:
        if li[0][2] == 'Orbit1':
            for ls in result_list:
                if ls[0][2] == 'Orbit4':
                    final_list = li+ls
                    for r1 in final_list:
                        for r2 in final_list:
                            if r1[1] == r2[1] and r1[2] == 'Orbit1' and r2[2]=='Orbit4':
                                total_time = r1[0]+r2[0]
                                result = [total_time,r1[1],'Hallitharam',r1[2],'RK Puram',r2[2],r1[3]]
                                route_result.append(result)
    

        if li[0][2] == 'Orbit2':
            for ls in result_list:
                if ls[0][2] == 'Orbit4':
                    final_list = li+ls
                    for r1 in final_list:
                        for r2 in final_list:
                            if r1[1] == r2[1] and  r1[2] == 'Orbit2' and r2[2] == 'Orbit4':
                                total_time = r1[0]+r2[0]
                                result = [total_time, r1[1],
                                          'Hallitharam', r1[2], 'RK Puram', r2[2], r1[3]]
                                route_result.append(result)

        if li[0][2] == 'Orbit3':
            for ls in result_list:
                if ls[0][2] == 'Orbit4':
                    final_list = li+ls
                    for r1 in final_list:
                        for r2 in final_list:
                            if r1[1] == r2[1] and  r1[2] == 'Orbit3' and r2[2] == 'Orbit4':
                                total_time = r1[0]+r2[0]
                                result = [total_time, r1[1],
                                          'RK Puram', r1[2], 'Hallitharam', r2[2], r1[3]]
                                route_result.append(result)

    #print route_result
    vc_un_sort = sorted(
        route_result, key=lambda route_result: route_result[-1], reverse=False)
    sorted_result = sorted(vc_un_sort, key=lambda vc_un_sort: vc_un_sort[0],reverse = False)
    print 'Vehicle '+sorted_result[0][1]+' to ' + \
        sorted_result[0][2]+' via '+sorted_result[0][3] + \
        ' and ' + sorted_result[0][4] + ' via ' + sorted_result[0][5]
                    


if __name__ == '__main__':
    result_list = []
    final_result = []
    in_weather = raw_input()
    weather_crater_percent, weather_vehicle_list = common_fun.get_weather_info(in_weather)
   
    in_orb_1 = raw_input()
    orbit_name, orbit_distance, orbit_crater, traffic_speed = common_fun.get_orbit_info(in_orb_1)
    result = common_fun.final_cal(orbit_name, weather_crater_percent, weather_vehicle_list, orbit_distance, orbit_crater, traffic_speed, result_list)
    final_result.append(result)
    result_list = []
    in_orb_2 = raw_input()
    orbit_name, orbit_distance, orbit_crater, traffic_speed = common_fun.get_orbit_info(in_orb_2)
    result = common_fun.final_cal(orbit_name, weather_crater_percent, weather_vehicle_list,orbit_distance, orbit_crater, traffic_speed, result_list)
    final_result.append(result)
    result_list = []
    in_orb_3 = raw_input()
    orbit_name, orbit_distance, orbit_crater, traffic_speed = common_fun.get_orbit_info(in_orb_3)
    result = common_fun.final_cal(orbit_name, weather_crater_percent, weather_vehicle_list, orbit_distance, orbit_crater, traffic_speed, result_list)
    final_result.append(result)
    result_list = []
    in_orb_4 = raw_input()
    orbit_name, orbit_distance, orbit_crater, traffic_speed = common_fun.get_orbit_info(in_orb_4)
    result = common_fun.final_cal(orbit_name, weather_crater_percent, weather_vehicle_list,orbit_distance, orbit_crater, traffic_speed, result_list)
    final_result.append(result)
    mission_possible(final_result)

