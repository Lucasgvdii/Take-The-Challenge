#The succession change detector problem. Link to the explanation and heading of the problem --> https://www.aceptaelreto.com/problem/statement.php?id=135

#Main function
def succession_change_detector(succession):

    changes=-1
    succession_constant=0.1
    last_val=0
    
    for i in range(len(succession)-1):
        current_val=succession[i]
        next_val=succession[i+1]
        if (current_val+succession_constant)%1000000!=next_val:
            succession_constant=(next_val-current_val)%1000000
            changes=changes+1
    return changes,(succession[-1]+succession_constant)%1000000


#You can obviously print these inside the function, but i personally to keep the code "print-free"
print(succession_change_detector([1,5,7,9,11])) # --> (1, 13)
print(succession_change_detector([1,2,3,4,5,6,7,8,10])) # --> (1, 12)
print(succession_change_detector([999996,999998,0,2,4])) # --> (0, 6)
print(succession_change_detector([10,9,8,7,3,2])) # --> (2, 1)
