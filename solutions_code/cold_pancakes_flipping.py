#The cold pancakes flipping problem. Link to the explanation and heading of the problem --> https://www.aceptaelreto.com/problem/statement.php?id=143

#Main function
def get_final_pancake_positions(pancakes, flip_heights):

    for i in flip_heights:
        
        pancakes_taken = pancakes[-i:]
        pancakes_left  = pancakes[:-i]
        
        pancakes_taken.reverse()
        pancakes = pancakes_left + pancakes_taken
        
    return pancakes

#You can obviously print these inside the function, but i personally to keep the code "print-free"
print(get_final_pancake_positions([5,4,3,2,1],[]))    # --> [5, 4, 3, 2, 1]
print(get_final_pancake_positions([5,4,3,2,1],[3,2])) # --> [5, 4, 1, 3, 2]
print(get_final_pancake_positions([5,4,3,2,1],[5]))   # --> [1, 2, 3, 4, 5]
