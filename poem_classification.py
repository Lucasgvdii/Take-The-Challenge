#The poem classification problem. Link to the explanation and heading of the problem --> https://www.aceptaelreto.com/problem/statement.php?id=110

#Main function
"""Given a poem, it returns its classification (according to its stanzas rhyme)"""
def classify_poem(poem):

    len_poem=len(poem)
    
    if len_poem>4:
        return "Too long"

    stanzas_c_rhyme=[]
    stanzas_a_rhyme=[]
    
    for i in poem:
        stanza_ryme=get_rhyme(i)
        if stanza_ryme==[]:
            return "No ryme"
        stanzas_c_rhyme.append([stanza_ryme[0]])
        stanzas_a_rhyme.append([stanza_ryme[1]])
        
    consonant_rhyme_table=get_rhymes_table(stanzas_c_rhyme)
    if len_poem==2:
        if consonant_rhyme_table.count(-1)==0:
            return "Pareado"
        return "Unknown"
    if len_poem==3:
        if consonant_rhyme_table.count(-1)==1:
            return "Terceto"
        return "Unknown"
    if len_poem==4:
        if consonant_rhyme_table.count(-1)==0:
            diff_rhymes=len(set(consonant_rhyme_table))
            if diff_rhymes==1:
                 return "Cuaderna Via"
            if diff_rhymes==2:
                if consonant_rhyme_table[0]==consonant_rhyme_table[2]:
                    return "Cuarteta"
                if consonant_rhyme_table[0]==consonant_rhyme_table[3]:
                    return "Cuarteto"
        if consonant_rhyme_table[1]==consonant_rhyme_table[3] and consonant_rhyme_table[1]==-1:
            asonant_rhyme_table=get_rhymes_table([stanzas_a_rhyme[1],stanzas_a_rhyme[3]])
            if asonant_rhyme_table[0]==asonant_rhyme_table[1]:
                return "Seguidilla"
        return "Unknown"

#Main auxiliar function
"""Given a list of rhymes relative to the poem stanzas, it returns a list of the relation between them. This list of rhymes can be either asonant (only vowels) or consonant,
   so the function will only return the rhyme table relative to the input value choice.
   F.E: [0,0,1,1,-1] In the result, when two or more positions share a number it implies the stanzas they respresent rhyme, and when there is a -1, it implies the stanza
   doesnt rhyme with anything."""
def get_rhymes_table(rhymes):

    aux_tables=get_tables(rhymes)
    rhyme_table=aux_tables[0]
    not_checked_table=aux_tables[1]
    discard_table=[]

    while not_checked_table!=[]:
                                                                    
        checking_rhyme=not_checked_table.pop(0)                            
        comparisons_number=len(not_checked_table)
        
        for i in range(comparisons_number):
            not_checked_rhyme=not_checked_table.pop(0)
            
            if rhymes[checking_rhyme]==rhymes[not_checked_rhyme]:
                rhyme_table[checking_rhyme]=checking_rhyme
                rhyme_table[not_checked_rhyme]=checking_rhyme
                
            else:
                rhyme_table[not_checked_rhyme]=-1
                discard_table.append(not_checked_rhyme)
                
        not_checked_table=discard_table
        discard_table=[]
        
    return rhyme_table
            
#Secondary auxiliar function
"""Given a stanza, it obtains the consonant and asonant rhyme from it (it is supposed that every word is "llana", which means it's stressed on its penultimate syllable).
   In order to make it a bit simpler, I used a generalized method to get the rhyming part of the words, which can be aplied for most "llanas" spanish words
   (getting the letters from the penultimate vowel, including itself), although there are quite a few exceptions """
def get_rhyme(stanza):
    
    vowels=["a","e","i","o","u"]
    consonants=["b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    
    vowel_count=0
    c_rhyme=""
    a_rhyme=""
    
    for i in range(len(stanza)):
        letter=stanza[-1-i]
        
        if letter in vowels:
            c_rhyme=letter+c_rhyme
            a_rhyme=letter+a_rhyme
            vowel_count=vowel_count+1
            if vowel_count==2:
                return [c_rhyme,a_rhyme]
            
        elif letter in consonants:
            c_rhyme=letter+c_rhyme
            
        elif letter==" ":
            return []
        
    return []

#Other auxiliar functions
"""In this fucntion i make two lists that will help me keep track of the rhyme comparisons i have made in the rhyme table function"""
def get_tables(rymes):
    table1=[]
    table2=[]
    for i in range(len(rymes)):
        table1.append(-1)
        table2.append(i)
    return [table1,table2]
              
#You can obviously print these inside the function"," but i personally like to keep the code "print-free"
print(classify_poem(["Historial ayer borrado","anteayer hubo pecado"]))
# --> Pareado
print(classify_poem(["Esto no pega","ni con cola."]))
# --> Unknown
print(classify_poem(["Era un simple clerigo, pobre de clerecia,","dicie cutiano missa de la sancta Maria;","non sabie decir otra, diciela cada dia,","mas la sabie por uso qe por sabiduria."]))
# --> Cuaderna Via
print(classify_poem(["Un manotazo duro, un golpe helado,","un hachazo invisible y homicida,","un empujon brutal te ha derribado."]))
# --> Terceto
print(classify_poem(["Era un simple clerigo, pobre de clerecie,","dicie cutiano missa de la sancta Marina;","non sabie decir otra, diciela cada diri,","mas la sabie por uso qe por sabiduria."]))
# --> Seguidilla
