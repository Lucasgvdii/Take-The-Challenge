#The light matches game problem. Link to the explanation and heading of the problem --> https://www.aceptaelreto.com/problem/statement.php?id=147

#Main function
def light_match_pick(matches, max_pick):

    my_pick=max_pick

    if matches==1:
        return "LOSE"
    
    while my_pick>0:
       if matches-my_pick==max_pick+1:
            my_pick=my_pick-1
       else:
           return my_pick
    return "LOSE"
                   
#You can obviously print these inside the function, but i personally to keep the code "print-free"
print(lucky_numbers(5,2)) # --> 1
print(lucky_numbers(4,3)) # --> 3
print(lucky_numbers(1,5)) # --> LOSE
