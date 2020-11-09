#The hobbits chain splitter problem. Link to the explanation and heading of the problem --> https://www.aceptaelreto.com/problem/statement.php?id=136

#Main function
def hobbits_chain_splitter(strength,chain_size):

    if chain_size<=strength*2:
        return 0

    first_half=0
    second_half=0
    cuts=1

    first_half=chain_size/3
    second_half=chain_size/3*2

    cuts=cuts+hobbits_chain_splitter(strength, first_half)
    cuts=cuts+hobbits_chain_splitter(strength, second_half)

    return cuts


#You can obviously print these inside the function, but i personally to keep the code "print-free"
print(hobbits_chain_splitter(10, 8)) # --> 0
print(hobbits_chain_splitter(5, 10)) # --> 0
print(hobbits_chain_splitter(1, 3))  # --> 1
print(hobbits_chain_splitter(1, 4))  # --> 2
