#The toy weight balance problem. Link to the explanation of the problem --> https://www.aceptaelreto.com/problem/statement.php?id=104

#Main function
def is_toy_balanced(child_toy):
    if weight_balance(child_toy)>=0:
        return "YES"
    return "NO"

#Auxiliar recursive function
def weight_balance(child_toy):

    base=child_toy.pop(0)
    left_weight=base[0]
    if left_weight==0:
        left_weight=weight_balance(child_toy)
        if left_weight==-1:
            return -1

    right_weight=base[2]
    if right_weight==0:
        right_weight=weight_balance(child_toy)
        if right_weight==-1:
            return -1

    if base[1]*left_weight-base[3]*right_weight==0:
        return left_weight+right_weight
    return -1

#You can obviously print these inside the function, but i personally like to keep the code "print-free"
print(is_toy_balanced([[0,2,0,4],[0,3,0,1],[1,1,1,1],[2,4,4,2],[1,6,3,2]])) # --> YES
print(is_toy_balanced([[0,1,3,4],[2,3,3,2]]))                               # --> NO
