#The periodic table problem. Link to the explanation and heading of the problem --> https://www.aceptaelreto.com/problem/statement.php?id=111

#Main function
def electron_configuration(name,element_num):
    electron_level_size=[2,2,6,2,6,2,10,6,2,10,6,2,12,10,6,2,12,10,6]
    electron_level_name=["1s","2s","2p","3s","3p","4s","3d","4p","5s","4d","5p","6s","4f","5d","6p","7s","5f","6d","7p"]
    cadena=""
    for i in range(len(electron_level_size)):
        if element_num-electron_level_size[i]>0:
            cadena=cadena+electron_level_name[i]+str(electron_level_size[i])+" "
            element_num=element_num-electron_level_size[i]
        else:
            cadena=cadena+electron_level_name[i]+str(element_num)
            break
    return cadena
           
#You can obviously print these inside the function, but i personally like to keep the code "print-free"
print(electron_configuration("cloro",17))
print(electron_configuration("calcio",20))
print(electron_configuration("rubidio",37))
print(electron_configuration("hierro",26))
