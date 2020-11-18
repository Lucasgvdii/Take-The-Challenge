#The broken keyboard problem. Link to the explanation and heading of the problem --> https://www.aceptaelreto.com/problem/statement.php?id=144

#Main function
def get_final_string(input_string):
    
    output_string=[]
    pos=0
    
    for i in input_string:
        if i == "3":
            if pos<len(output_string):
                output_string.pop(pos)
        elif i == "-":
            pos=0
        elif i == "+":
            pos=len(output_string)
        elif i == "*":
            if pos!=len(output_string):
                pos=pos+1
        else:
            output_string.insert(pos,i)
            pos=pos+1
    return list2str(output_string)

def list2str(klist):
    string=""
    for i in klist:
        string=string+i
    return string
    
#You can obviously print these inside the function, but i personally to keep the code "print-free"
print(get_final_string("EDA"))       # --> EDA
print(get_final_string("EDA-333"))   # --> " " //Nothing
print(get_final_string("dD-3*A-E+")) # --> EDA
print(get_final_string("EDA-3E*3A")) # --> EDA
