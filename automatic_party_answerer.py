#The automatic party answerer problem. Link to the explanation and heading of the problem --> https://www.aceptaelreto.com/problem/statement.php?id=117

#Main function
def party_answerer(party_introductions):
    answer=""
    for i in party_introductions:
        answer=answer+"Hello "+i[4:]+".\n"
    return answer
          
#You can obviously print these inside the function, but i personally like to keep the code "print-free"
print(party_answerer(["Soy Lotario","Soy Aldonza"]))         # --> Hello Lotario. Hello Aldonza.
print(party_answerer(["Soy Carlos","Soy Diego","Soy Hugo"])) # --> Hello Carlos. Hello Diego. Hello Hugo.
