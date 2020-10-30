#The hostel beds problem. Link to the explanation and heading of the problem --> https://www.aceptaelreto.com/problem/statement.php?id=127

#Main function
def hostel_beds_problem(names,beds,song_words_num):
    current_pos=0
    if beds>=len(names):
        return "They all have bed"
    if beds==0:
        return "None have bed"
    while len(names) > beds:
        ending_pos=(current_pos+song_words_num-1)%len(names)
        current_pos=ending_pos%len(names)
    return names
    
#You can obviously print these inside the function, but i personally to keep the code "print-free"
print(hostal_beds_problem(["Anastasio","Ignacio","Felipe","Borja","Daniel","Cesar"],2,3))                   # --> ['Anastasio', 'Daniel']
print(hostal_beds_problem(["Javier","Ramiro","Luis","Rosa","Carmen","Paola","Josefa"],0,3))                 # --> None has bed
print(hostal_beds_problem(["Petra","Santiago","Pepi"],2,20))                                                # --> ['Petra', 'Pepi']
print(hostal_beds_problem(["Merche","Juanjo","Miriam","Pilar","Marina","Ovidio","Rafael","Eustaquio"],4,7)) # --> ['Merche', 'Miriam', 'Pilar', 'Marina']
