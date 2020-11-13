#The parentheses balancing problem. Link to the explanation and heading of the problem --> https://www.aceptaelreto.com/problem/statement.php?id=141

#Main function
def are_parentheses_balanced(string):

    if is_balanced(string,"")[0]:
       return "YES"
    return "NO"
        
    
def is_balanced(string,symbol):
    
    balance=[True,string]
    while string!="":

        if balance[0]:
            string=balance[1]
        else:
            return False,""
        
        for i in range(len(string)):
            
            if string[i]=="(" or string[i]=="[" or string[i]=="{":
                balance=is_balanced(string[i+1:],string[i])
                break;
            
            elif string[i]==")":
                if symbol=="(":
                    return True,string[i+1:]
                return False,string[i+1:]
            
            elif string[i]=="]":
                if symbol=="[":
                    return True,string[i+1:]
                return False,string[i+1:]
            
            elif string[i]=="}":
                if symbol=="{":
                    return True,string[i+1:]
                return False,string[i+1:]
            
            elif i==len(string)-1:
                string=""
                
    return True,""

#You can obviously print these inside the function, but i personally to keep the code "print-free"
print(are_parentheses_balanced("({[]})()"))                                                       # --> YES
print(are_parentheses_balanced("Tengase en cuenta (obviamente) que puede haber otros simbolos.")) # --> YES
print(are_parentheses_balanced(":)"))                                                             # --> NO
