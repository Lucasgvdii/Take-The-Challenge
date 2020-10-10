#The cesar encryption vowels problem. Link to the explanation of the problem --> https://www.aceptaelreto.com/problem/statement.php?id=102&cat=53

#Main function
def cesar_vowels(string):
    alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    string=string.lower()
    
    cesar_key=string[0]
    cesar_deplacement=-15
    
    for letter in alphabet:
        if letter==cesar_key:
            break
        cesar_deplacement=cesar_deplacement+1

    counted_vowels=0
    
    for i in string:
        for letter in range(len(alphabet)):
            if i==alphabet[letter]:
                
                #Uncomment this line if you want to see the "uncoded" string
                #print(alphabet[(letter-cesar_deplacement)%26],end='')
                
                if is_vowel(alphabet[(letter-cesar_deplacement)%26]):
                     counted_vowels=counted_vowels+1
                break
    return counted_vowels

#Auxiliar function
def is_vowel(letter):
    if letter=="a" or letter=="e" or letter=="i" or letter=="o" or letter=="u":
        return True
    return False

#You can obviously print these inside the function, but i personally like to keep the code "print-free"
print(cesar_vowels("pEsta cadena esta sin codificar")) # --> 12
print(cesar_vowels("pfin"))                            # --> 1
print(cesar_vowels("qbfjpvBFJPV"))                     # --> 10
print(cesar_vowels("ozdhntZDHNT"))                     # --> 10
print(cesar_vowels("xXzwoziui-Um"))                    # --> 4
print(cesar_vowels("qGJO"))                            # --> 1
