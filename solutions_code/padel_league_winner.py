#The padel league winner problem. Link to the explanation and heading of the problem --> https://www.aceptaelreto.com/problem/statement.php?id=109

#Imports
from math import factorial

#Main function
def padel_winner(match_list):
    list_of_teams=get_teams(match_list)
    
    winner_list=[]
    looser_list=[]
    for i in match_list:
        if i[1]>i[3]:
            winner_list.append(i[0])
            looser_list.append(i[2])
        else:
            winner_list.append(i[2])
            looser_list.append(i[0])

    winner=""
    max_points=0

    for i in list_of_teams:
        victories=winner_list.count(i)
        looses=looser_list.count(i)
        points=victories*2+looses
        if points>max_points:
            winner=i
            max_points=points
            not_played=factorial(len(list_of_teams)-1)*2-len(match_list)
        elif points==max_points:
            winner="Tie"
            max_points=points
            not_played=0

    return winner+" "+str(not_played)

def get_teams(match_list):
    list_of_teams=[]
    for i in match_list:
        if i[0] not in list_of_teams:
            list_of_teams.append(i[0])
        if i[2] not in list_of_teams:
            list_of_teams.append(i[2])
    return set(list_of_teams)
        
              
#You can obviously print these inside the function, but i personally like to keep the code "print-free"
print(padel_winner([["Buenisimos",3,"Malisimos",0],["Buenillos",2,"Malillos",1],["Buenillos",3,"Malisimos",0],["Buenisimos",3,"Malillos",0],["Buenisimos",2,"Buenillos",1],
                    ["Malisimos",0,"Buenisimos",3],["Malillos",1,"Buenillos",2],["Malisimos",0,"Buenillos",3],["Malillos",0,"Buenisimos",3],["Buenillos",1,"Buenisimos",2]])) # --> Buenisimos 2  
print(padel_winner([["Abuelos",3,"Abueletes",0],["Abueletes",2,"Abuelos",1]]))                                                                                                # --> Tie 0
