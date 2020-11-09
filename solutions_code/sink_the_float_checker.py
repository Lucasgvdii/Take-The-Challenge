#The sink the float checker problem. Link to the explanation and heading of the problem --> https://www.aceptaelreto.com/problem/statement.php?id=137

#Main function
def sink_the_float_checker(boat_sizes,gameboard_size,gameboard):

    if len(gameboard)!=gameboard_size:
        return "No"

    detected_boats=0
    detected_boat_sizes=[]

    for y in range(len(gameboard)):
        for x in range(len(gameboard[0])):
            if gameboard[y][x]==1:
                detected_boats=detected_boats+1
                result=get_boat_length(x,y,gameboard)
                gameboard=result[1]
                detected_boat_sizes.append(result[0])
                
    detected_boat_sizes.sort()
    boat_sizes.sort()
    
    if detected_boat_sizes==boat_sizes:
        return "Yes"
    return "No"               

def get_boat_length(coordinate_x,coordinate_y,gameboard):
    
    boat_length=1
    gameboard[coordinate_y][coordinate_x]=2
    rest_of_boat=[0,gameboard]

    if coordinate_x+1<=len(gameboard[0]) and gameboard[coordinate_y][coordinate_x+1]==1:
        rest_of_boat=get_boat_length(coordinate_x+1,coordinate_y,gameboard)
    
    elif coordinate_x+1<=len(gameboard[0]) and coordinate_y+1<=len(gameboard) and gameboard[coordinate_y+1][coordinate_x+1]==1:
        rest_of_boat=get_boat_length(coordinate_x+1,coordinate_y+1,gameboard)
    
    elif coordinate_y+1<=len(gameboard) and gameboard[coordinate_y+1][coordinate_x]==1:
        rest_of_boat=get_boat_length(coordinate_x,coordinate_y+1,gameboard)
     
    elif coordinate_x-1>=0 and coordinate_y+1<=len(gameboard) and gameboard[coordinate_y+1][coordinate_x-1]==1:
        rest_of_boat=get_boat_length(coordinate_x-1,coordinate_y+1,gameboard)

    boat_length=boat_length+rest_of_boat[0]
    return [boat_length,rest_of_boat[1]]

#You can obviously print these inside the function, but i personally to keep the code "print-free"
print(sink_the_float_checker([2,3],6,[[0,1,1,0,0,0],[0,0,0,0,0,0],[0,0,0,1,0,0],[0,0,0,1,0,0],[0,0,0,1,0,0],[0,0,0,0,0,0]])) # --> Yes
print(sink_the_float_checker([2,3],5,[[0,1,1,1,0],[0,0,0,0,1],[0,0,0,0,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]))             # --> No
