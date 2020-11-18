#The love train couples problem. Link to the explanation and heading of the problem --> https://www.aceptaelreto.com/problem/statement.php?id=145

#Main function
def love_train_couples(train):
    
    train=str2mat(train)
    train_check=[]
    total=0
    while train_check!=train:
        
        couples=[]
        train_check=[]+train
        
        for i in range(len(train)-1):
            
            if train[i]=="H":
                if train[i+1]=="M":
                    couples.append(i)
                    couples.append(i+1)
                elif train[i+1]!="m" and train[i+1]!="H" and train[i+1]!="h" and train[i+1]!="@":
                    train[i+1]=train[i]
                    train[i]=" "
                    
            elif train[i]=="h":
                if train[i+1]=="m":
                    couples.append(i)
                    couples.append(i+1)
                elif train[i+1]!="M" or train[i+1]!="H" and train[i+1]!="h" and train[i+1]!="@":
                    train[i+1]=train[i]
                    train[i]=" "
                    
        for i in couples:
            train[i]=" "
        total=total+len(couples)/2
    return total
                            
def str2mat(string):
    mat=[]
    for i in string:
        mat.append(i)
    return mat
                
                   
#You can obviously print these inside the function, but i personally to keep the code "print-free"
print(love_train_couples("H.$.*M"))    # --> 1
print(love_train_couples("H==@M"))     # --> 0
print(love_train_couples("MHMHMHHMM")) # --> 4
