#The no-loser of recipe bets problem. Link to the explanation and heading of the problem --> https://www.aceptaelreto.com/problem/statement.php?id=118

#Imports
import math

#Main function
def get_number_of_recipes(bets):
    
    pilar=bets[0]
    marco=bets[1]
    pedro=bets[2]

    if pedro==marco:
        if pedro==pilar:
            return 0
        if pedro<pilar:
            return check_result(get_max_recipes(pedro,1,pilar))
        if pedro>pilar:
            return check_result(get_min_recipes(pedro,1,pilar))
    if pedro==pilar:
        if pedro<marco:
            return check_result(get_max_recipes(pedro,1,marco))
        return check_result(get_min_recipes(pedro,1,marco))
    if pedro<marco:
        if pedro<pilar:
            if marco<pilar:
                return check_result(get_min_recipes(pedro,0,pilar))
            return check_result(get_min_recipes(pedro,0,marco))
        return 0
    if pedro>pilar:
        if marco>pilar:
            return check_result(get_max_recipes(pedro,0,pilar))
        return check_result(get_max_recipes(pedro,0,marco))
    return 0

#Auxiliar functions
"""This functions literally represent the mathematical function that would solve the problem if you did it by hand"""
def get_min_recipes(pedro,friends_with_same_bet_as_pedro,max_bet_friend):
    return math.ceil(((pedro+(max_bet_friend-pedro)/2)*3-64*(2-friends_with_same_bet_as_pedro))/(2/(2-friends_with_same_bet_as_pedro)))-1

def get_max_recipes(pedro,friends_with_same_bet_as_pedro,min_bet_friend):
    return math.floor(((min_bet_friend+(pedro-min_bet_friend)/2)*3)/(2/(2-friends_with_same_bet_as_pedro)))+1

def check_result(num_recipes):
    if num_recipes>64 or num_recipes<0:
        return "I"
    return num_recipes
        
          
#You can obviously print these inside the function, but i personally to keep the code "print-free"
print(get_number_of_recipes([5,17,32]))  # --> 56
print(get_number_of_recipes([5,32,17]))  # --> 0
print(get_number_of_recipes([32,17,5]))  # --> I
print(get_number_of_recipes([60,55,50])) # --> 36
