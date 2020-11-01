#The umbrella building materials problem. Link to the explanation and heading of the problem --> https://www.aceptaelreto.com/problem/statement.php?id=128

#Main function
def get_sticks_and_scraps(stick_len,umbrellas):
    stick_num=0
    scraps_total_len=0
    current_scrap=0
    for i in umbrellas:
        umbrella_radius_sticks=i[0]*i[1]
        umbrella_radius_length=i[2]
        if umbrella_radius_length>stick_len:
            return "Impossible"
        for x in range(umbrella_radius_sticks):
            if current_scrap<umbrella_radius_length:
                stick_num=stick_num+1
                scraps_total_len=scraps_total_len+current_scrap
                current_scrap=stick_len-umbrella_radius_length
            else:
                current_scrap=current_scrap-umbrella_radius_length
    return stick_num,scraps_total_len+current_scrap
            
#You can obviously print these inside the function, but i personally to keep the code "print-free"
print(get_sticks_and_scraps(200,[[8,1,60],[8,3,20]])) # --> (5, 40)
print(get_sticks_and_scraps(100,[[8,1,60],[8,3,20]])) # --> (13, 340)      
print(get_sticks_and_scraps(50, [[8,1,60],[8,3,20]])) # --> Impossible
print(get_sticks_and_scraps(20, [[8,1,60],[8,3,20]])) # --> Impossible
