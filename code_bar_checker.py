#The code bar problem. Link to the explanation and heading of the problem --> https://www.aceptaelreto.com/problem/statement.php?id=106

#Main function
def code_bar_checker(codebar):
    codebar_str=zero_filler(str(codebar))
    return check_codebar(codebar_str)    

#Main auxiliar function
def check_codebar(codebar):
    length_num=len(codebar)
    key_value=0
    for i in range(length_num-1):
        if i%2==0:
            key_value=key_value+3*int(codebar[length_num-2-i])
        else:
            key_value=key_value+int(codebar[length_num-2-i])
    if (key_value+int(codebar[-1]))%10==0:
        if length_num==8:
            return "YES"
        return "YES "+code_bar_country(codebar[:3])
    return "NO"

#Basic auxiliar functions
def zero_filler(codebar):
    if len(codebar)==8 or len(codebar)==13:
        return codebar
    return zero_filler("0"+codebar)
      
def code_bar_country(codebar):
    if codebar[0]=="0":
        return "EEUU"
    if codebar[:2]=="50":
        return "England"
    if codebar[:2]=="70":
        return "Norway"
    if codebar[:3]=="50":
        return "Bulgary"
    if codebar[:3]=="380":
        return "Ireland"
    if codebar[:3]=="539":
        return "Portugal"
    if codebar[:3]=="560":
        return "Venezuela"
    if codebar[:3]=="850":
        return "Cuba"
    if codebar[:3]=="890":
        return "India"
    else:
        return "Unknown"
    
#You can obviously print these inside the function, but i personally like to keep the code "print-free"
print(code_bar_checker(65839522))       # --> YES
print(code_bar_checker(65839521))       # --> NO
print(code_bar_checker(8414533043847))  # --> YES Unknown
print(code_bar_checker(5029365779425))  # --> YES England    
print(code_bar_checker(5129365779425))  # --> NO
