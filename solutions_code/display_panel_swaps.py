#The display panel swaps problem. Link to the explanation and heading of the problem --> https://www.aceptaelreto.com/problem/statement.php?id=129

#Main function
def display_panel_swaps(digits):
    
    nums_led =[[1,1,1,1,1,1,0], #0
               [0,0,1,1,0,0,0], #1 
               [0,1,1,0,1,1,1], #2
               [0,1,1,1,1,0,1], #3
               [1,0,1,1,0,0,1], #4
               [1,1,0,1,1,0,1], #5
               [1,1,0,1,1,1,1], #6
               [0,1,1,1,0,0,0], #7
               [1,1,1,1,1,1,1], #8
               [1,1,1,1,0,0,1]] #9

    empty_led =[0,0,0,0,0,0,0]  #empty

    digits_len=len(digits)
    display=[]
    led_changes=0
    
    for i in range(digits_len):
        display.append(empty_led)
        digits=digits+"X"       #we add as many X as digits in the number given in representation for the empty
                                #led slots there will be when the number starts to dissapear from the display
        
    for i in range(digits_len+digits_len):
        for x in range(digits_len):
            if x!=digits_len-1:
                led_changes=led_changes+display_swaps(display[x],display[x+1])
                display[x]=display[x+1]
            else:
                if digits[i]=="X":
                    led_changes=led_changes+display_swaps(display[x],empty_led)
                    display[x]=empty_led
                else:
                    led_changes=led_changes+display_swaps(display[x],nums_led[int(digits[i])])
                    display[x]=nums_led[int(digits[i])]
    return led_changes

#Auxiliar function
def display_swaps(previous_num,actual_num):
    swaps=0
    for j in range(len(previous_num)):
        if actual_num[j]!=previous_num[j]:
            swaps=swaps+1
    return swaps
        
#You can obviously print these inside the function, but i personally to keep the code "print-free"
print(display_panel_swaps("123"))  # --> 42
print(display_panel_swaps("305"))  # --> 48      
print(display_panel_swaps("1"))    # --> 4
print(display_panel_swaps("1233")) # --> 56
