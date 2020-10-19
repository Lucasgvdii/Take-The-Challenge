#The semaphore road problem. Link to the explanation and heading of the problem --> https://www.aceptaelreto.com/problem/statement.php?id=113

#Main function
"""We obtain the maximum speed a car can go in the road. After that, we check if with that
   speed it can go through every traffic light without stopping. If it can, we return how
   many seconds does it take to get to the end of the road at that speed."""
def traffic_light_avoiding_optimal_speed(speed,traffic_light_data):
    max_speed=getMaxSpeed(speed,traffic_light_data)
    while max_speed>=0.1:
        road_length=0
        for traffic_light in traffic_light_data:
            road_length=road_length+traffic_light[0]
            if not inTimeRange(max_speed,road_length,traffic_light[1],traffic_light[2]):
                break
            if traffic_light == traffic_light_data[-1]:
                return road_length/max_speed
        max_speed=max_speed-0.1
            
    return "Impossible"

#Main auxiliar function
"""Given a speed and the data of the traffic light, this function checks if a car, at that
   speed, will reach the height of the traffic light on the street in one of its opening
   intervals or not."""
def inTimeRange(speed,dist,closed_time,open_time):
    if open_time==0: return False
    cont=1
    time=dist/speed
    #Uncomment this line to see the time at which the car arrives to the traffic light
    #print(time)
    while closed_time*cont+open_time*(cont-1)<=time:
        #Uncomment this line to see the opening interval times of the traffic light
        #print("["+str(tc*cont+ta*(cont-1))+","+str(tc*cont+ta*(cont))+"]")
        if closed_time*cont+open_time*(cont-1)<=time and closed_time*cont+open_time*(cont)>=time:
            return True
        if closed_time*cont+open_time*(cont-1)<time:
            cont=cont+1
    return False

#Other auxiliar functions
"""Gets the highest speed a car can go in order to go through all semaphores without stopping"""
def getMaxSpeed(speed,traffic_light_data):
    global_max_speed=speed
    road_length=0
    for traffic_light in traffic_light_data:
        road_length=road_length+traffic_light[0]
        traffic_light_max_speed=road_length/traffic_light[1]
        if traffic_light_max_speed<global_max_speed:
            global_max_speed=traffic_light_max_speed
    return global_max_speed
        
           
#You can obviously print these inside the function but i personally like to keep the code "print-free"
print(traffic_light_avoiding_optimal_speed(10,[[50,10,4],[50,10,10]]))         # --> 20
print(traffic_light_avoiding_optimal_speed(4,[[50,10,4],[50,10,10]]))          # --> 50
print(traffic_light_avoiding_optimal_speed(10,[[10,110,100]]))                 # --> Impossible
print(traffic_light_avoiding_optimal_speed(10,[[100,31,1],[1,30,1],[1,31,1]])) # --> Impossible
