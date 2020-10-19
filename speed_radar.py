#The speed radar problem. Link to the explanation and heading of the problem --> https://www.aceptaelreto.com/problem/statement.php?id=112

#Main function
def highway_speed_regulation(distance,max_speed,seconds):
    print(distance/seconds)
    max_speed=max_speed*1000/3600
    if distance<0 or max_speed<0 or seconds<0:
        return "ERROR"
    if distance/seconds<=max_speed:
        return "OK"
    if distance/seconds<=max_speed*1.2:
        return "FEE"
    return "PERMIT POINTS"
           
#You can obviously print these inside the function, but i personally like to keep the code "print-free"
print(highway_speed_regulation(9165,110,300))
print(highway_speed_regulation(9165,110,299))
print(highway_speed_regulation(12000,100,433))
print(highway_speed_regulation(12000,100,431))
print(highway_speed_regulation(12000,100,359))
print(highway_speed_regulation(-1000,-50,-100))

