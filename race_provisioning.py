#The race provisioning problem. Link to the explanation and heading of the problem --> https://www.aceptaelreto.com/problem/statement.php?id=122

#Main function
def establish_provisioning_km(race_heights):
    plains_km=[]
    current_km=-1
    for i in range(len(race_heights)-1):
        if race_heights[i]==race_heights[i+1]:
            if current_km==-1:
                current_km=i
            plains_km.append(current_km)
        else:
            current_km=-1
            
    if plains_km==[]:
        return "No provisioning today fellas"
    
    provisioning_km=longuest_plain(plains_km)
    return provisioning_km, plains_km.count(provisioning_km)
            
def longuest_plain(plains_km): 
    return max(plains_km, key = plains_km.count)        
        
          
#You can obviously print these inside the function, but i personally to keep the code "print-free"
print(establish_provisioning_km([0,50,50,50,100]))  # --> (1,2)
print(establish_provisioning_km([10,10]))           # --> (0,1)
print(establish_provisioning_km([0,5]))             # --> No provisioning today fellas
print(establish_provisioning_km([0,50,50,100,100])) # --> (1,1)
print(establish_provisioning_km([0,50,50,3,3,3]))   # --> (3,2)
