#The gum offer problem. Link to the explanation and heading of the problem --> https://www.aceptaelreto.com/problem/statement.php?id=121

#Main function
def get_total_gums(gums_required,gums_given,gums_bought):
    total_gums=gums_bought
    resting_gums=gums_bought
    if gums_given>=gums_required and gums_bought>=gums_required:
        return "bankruptcy"
    while resting_gums!=0:
        if resting_gums<gums_required:
            break
        x=resting_gums//gums_required
        resting_gums=resting_gums%gums_required+x*gums_given
        total_gums=total_gums+x*gums_given
    return total_gums,resting_gums      
          
#You can obviously print these inside the function, but i personally to keep the code "print-free"
print(get_total_gums(5,1,25))   # --> (31, 1)
print(get_total_gums(5,1,5))    # --> (6, 1)
print(get_total_gums(10,1,100)) # --> (111, 1)
print(get_total_gums(2,5,20))   # --> bankruptcy
