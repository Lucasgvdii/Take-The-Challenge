#The hello world addict problem. Link to the explanation and heading of the problem --> https://www.aceptaelreto.com/problem/statement.php?id=116

#Main function
def hello_world_spammer(num):
    string=""
    for i in range(num):
        string=string+"Hello world!\n"
    return string
          
#You can obviously print these inside the function, but i personally like to keep the code "print-free"
print(hello_world_spammer(23))  # --> Hello world x 23
print(hello_world_spammer(2))   # --> Hello world x 2
print(hello_world_spammer(5))   # --> Hello world x 5
print(hello_world_spammer(17))  # --> Hello world x 17
print(hello_world_spammer(321)) # --> Hello world x 321
