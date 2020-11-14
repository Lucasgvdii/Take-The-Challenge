#The hide and seek catcher selection problem. Link to the explanation and heading of the problem --> https://www.aceptaelreto.com/problem/statement.php?id=142

#Main function
def who_seeks(num_of_children, jumps):

    children=[]
    for i in range(num_of_children):
        children.append(i)

    cont=0
    while len(children)!=1:
        cont=(cont+jumps)%len(children)
        children.pop(cont)
        
    return children[0]+1

#You can obviously print these inside the function, but i personally to keep the code "print-free"
print(who_seeks(4,1))  # --> 1
print(who_seeks(7,2))  # --> 4
print(who_seeks(10,2)) # --> 4
