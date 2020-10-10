#The function inheritance problem. Link to the explanation of the problem --> https://www.aceptaelreto.com/problem/statement.php?id=103&cat=53

#Main function
def is_equitative(grade,polynomial,n_rectangles):

    cain_area=0
    rectangle_base_size=1/n_rectangles

    for x in range(n_rectangles):
        fx=0
        rectangle_x_area=0
        
        for i in range(len(polynomial)):
            fx=fx+pow(x*rectangle_base_size,grade-i)*polynomial[i]
            
        if fx>0:
            rectangle_x_area=min(fx,1)*rectangle_base_size
            
        cain_area=cain_area+rectangle_x_area
        
    abel_area=1-cain_area
    diference=abel_area-cain_area
    
    if diference>=0.001:
        return "ABEL"
    elif diference<=-0.001:
        return "CAIN"
    return "equitative"

#You can obviously print these inside the function, but i personally like to keep the code "print-free"
print(is_equitative(1,[1,0],100))        # --> ABEL
print(is_equitative(3,[1,2,-1,0],1000))  # --> ABEL
print(is_equitative(3,[1,2,-1,1],1000))  # --> CAIN
print(is_equitative(1,[3,-1],10000))     # --> equitative
print(is_equitative(1,[3,-1],2))         # --> ABEL
