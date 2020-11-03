#The diagonal deplacement obsession problem. Link to the explanation and heading of the problem --> https://www.aceptaelreto.com/problem/statement.php?id=130

#Main function
def number_of_deplacements(lateral_size,act_pos,tar_pos):
    different_dir_deplacements=0
    current_direction=""
    if (abs(act_pos[0]-tar_pos[0])+abs(act_pos[1]-tar_pos[1]))%2!=0:
        return "Impossible"
    while act_pos!=tar_pos:
        result=dir_choice(lateral_size,act_pos,tar_pos)
        act_pos=result[0]
        if current_direction != result[1]:
            current_direction = result[1]
            different_dir_deplacements=different_dir_deplacements+1
    return steps

#Auxiliar function
def dir_choice(lateral_size,act_pos,tar_pos):
    dif_x=act_pos[0]-tar_pos[0]
    dif_y=act_pos[1]-tar_pos[1]
    if dif_x>0 or act_pos[0]+1>lateral_size:
        if dif_y>0 or act_pos[1]+1>lateral_size:
            return [[act_pos[0]-1,act_pos[1]-1],"down-left"]
        else:
            return [[act_pos[0]-1,act_pos[1]+1],"up-left"]
    else:
        if dif_y>0 or act_pos[1]+1>lateral_size:
            return [[act_pos[0]+1,act_pos[1]-1],"down-right"]
        else:
            return [[act_pos[0]+1,act_pos[1]+1],"up-right"]


#You can obviously print these inside the function, but i personally to keep the code "print-free"
print(number_of_deplacements(5,[1,2],[4,3]))  # --> 2
print(number_of_deplacements(5,[1,2],[3,0]))  # --> 1      
print(number_of_deplacements(10,[0,0],[0,1])) # --> Impossible
