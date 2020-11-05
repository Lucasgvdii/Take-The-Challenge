#The grandpa's letters problem. Link to the explanation and heading of the problem --> https://www.aceptaelreto.com/problem/statement.php?id=131

#Main function
def are_repeated_characters(text,pos1,pos2):
    
    equal="NO"
    initial_pos=min(pos1,pos2)
    final_pos=max(pos1,pos2)

    for i in range(initial_pos,final_pos):
        if text[i]==text[i+1]:
            equal="YES"
        else:
            break    
    return equal

#You can obviously print these inside the function, but i personally to keep the code "print-free"
print(are_repeated_characters("Hooolaa",0,6)) # --> NO
print(are_repeated_characters("Hooolaa",1,3)) # --> YES
print(are_repeated_characters("Hooolaa",3,2)) # --> YES
print(are_repeated_characters("Hooolaa",1,2)) # --> YES
print(are_repeated_characters("Adios",1,2))   # --> NO
