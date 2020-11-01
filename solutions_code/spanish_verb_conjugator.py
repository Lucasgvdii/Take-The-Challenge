#The spanish verb conjugator problem. Link to the explanation and heading of the problem --> https://www.aceptaelreto.com/problem/statement.php?id=123

#Main function
def spanish_verb_conjugator(verb,tense):
    verb_ending=verb[-2]+verb[-1]
    verb_root=verb[0:-2]
    if tense=="A":
        return present_tense(verb_root,verb_ending)
    if tense=="P":
        return past_simple_tense(verb_root,verb_ending)
    if tense=="F":
        return future_tense(verb_root,verb_ending)
    
#Auxiliar functions            
def present_tense(verb_root,verb_ending): 
    conjugation=""
    if verb_ending=="ar":
        conjugation=conjugation+"Yo "+verb_root+"o - "
        conjugation=conjugation+"Tu "+verb_root+"as - "
        conjugation=conjugation+"El "+verb_root+"a - "
        conjugation=conjugation+"Nosotros "+verb_root+"amos - "
        conjugation=conjugation+"Vosotros "+verb_root+"ais - "
        conjugation=conjugation+"Ellos "+verb_root+"an"
        return conjugation
    conjugation=conjugation+"Yo "+verb_root+"o - "
    conjugation=conjugation+"Tu "+verb_root+"es - "
    conjugation=conjugation+"El "+verb_root+"e - "
    if verb_ending=="er":
        conjugation=conjugation+"Nosotros "+verb_root+"emos - "
        conjugation=conjugation+"Vosotros "+verb_root+"eis - "
    else:
        conjugation=conjugation+"Nosotros "+verb_root+"imos - "
        conjugation=conjugation+"Vosotros "+verb_root+"is - "  
    conjugation=conjugation+"Ellos "+verb_root+"en"
    return conjugation

def past_simple_tense(verb_root,verb_ending): 
    conjugation=""
    if verb_ending=="ar":
        conjugation=conjugation+"Yo "+verb_root+"e - "
        conjugation=conjugation+"Tu "+verb_root+"aste - "
        conjugation=conjugation+"El "+verb_root+"o - "
        conjugation=conjugation+"Nosotros "+verb_root+"amos - "
        conjugation=conjugation+"Vosotros "+verb_root+"asteis - "
        conjugation=conjugation+"Ellos "+verb_root+"aron"
        return conjugation
    conjugation=conjugation+"Yo "+verb_root+"i - "
    conjugation=conjugation+"Tu "+verb_root+"iste - "
    conjugation=conjugation+"El "+verb_root+"io - "
    conjugation=conjugation+"Nosotros "+verb_root+"imos - "
    conjugation=conjugation+"Vosotros "+verb_root+"isteis - "
    conjugation=conjugation+"Ellos "+verb_root+"ieron"
    return conjugation

def future_tense(verb_root,verb_ending): 
    conjugation=""
    conjugation=conjugation+"Yo "+verb_root+verb_ending[0]+"re - "
    conjugation=conjugation+"Tu "+verb_root+verb_ending[0]+"ras - "
    conjugation=conjugation+"El "+verb_root+verb_ending[0]+"ra - "
    conjugation=conjugation+"Nosotros "+verb_root+verb_ending[0]+"remos - "
    conjugation=conjugation+"Vosotros "+verb_root+verb_ending[0]+"reis - "
    conjugation=conjugation+"Ellos "+verb_root+verb_ending[0]+"ran"
    return conjugation
        
          
#You can obviously print these inside the function, but i personally to keep the code "print-free"
print(spanish_verb_conjugator("saltar","P"))   # --> Yo salte - Tu saltaste - El salto - Nosotros saltamos - Vosotros saltasteis - Ellos saltaron
print(spanish_verb_conjugator("comer","A"))    # --> Yo como - Tu comes - El come - Nosotros comemos - Vosotros comeis - Ellos comen
print(spanish_verb_conjugator("vivir","F"))    # --> Yo vivire - Tu viviras - El vivira - Nosotros viviremos - Vosotros vivireis - Ellos viviran
print(spanish_verb_conjugator("terminar","A")) # --> Yo termino - Tu terminas - El termina - Nosotros terminamos - Vosotros terminais - Ellos terminan
