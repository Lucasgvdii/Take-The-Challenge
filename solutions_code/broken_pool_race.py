#The broken pool race problem. Link to the explanation and heading of the problem --> https://www.aceptaelreto.com/problem/statement.php?id=131

#Main function
def broken_pool_race(our_pool,neighbour_pool):
    
    if our_pool[1]<our_pool[2]:
        if neighbour_pool[1]<neighbour_pool[2]:
            return "Impossible to fill"
        
    our_filling_target=our_pool[0]
    our_travel_balance=our_pool[1]-our_pool[2]
    
    neighbour_filling_target=neighbour_pool[0]
    neighbour_travel_balance=neighbour_pool[1]-neighbour_pool[2]
    
    our_current_filling=our_pool[1]
    neighbour_current_filling=neighbour_pool[1]
    
    trips=1
    
    while our_current_filling<our_filling_target and neighbour_current_filling<neighbour_filling_target:
        our_current_filling=our_current_filling+our_travel_balance
        neighbour_current_filling=neighbour_current_filling+neighbour_travel_balance
        trips=trips+1
        
    if our_current_filling>=our_filling_target:
        if neighbour_current_filling>=neighbour_filling_target:
            return "Tie "+str(trips)
        return "We win "+str(trips)
    return "Neighbour wins "+str(trips)

#You can obviously print these inside the function, but i personally to keep the code "print-free"
print(broken_pool_race([10,5,1],[15,6,1])) # --> Tie 3
print(broken_pool_race([50,5,1],[50,5,0])) # --> Neighbour wins 10    
print(broken_pool_race([50,5,1],[50,5,6])) # --> We win 13 
