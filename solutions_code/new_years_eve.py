#The new years eve problem. Link to the explanation and heading of the problem --> https://www.aceptaelreto.com/problem/statement.php?id=148

#Main function
def minutes_left(hour):

    h=int(hour[:2])
    m=int(hour[3:])

    h=24-h

    if m!=0:
        h=h-1
        m=60-m
        
    return h*60+m
                   
#You can obviously print these inside the function, but i personally to keep the code "print-free"
print(minutes_left("23:45")) # --> 15
print(minutes_left("21:30")) # --> 150
print(minutes_left("00:01")) # --> 1439
