#The straight flush missing card problem. Link to the explanation and heading of the problem --> https://www.aceptaelreto.com/problem/statement.php?id=134

#Main function
def straight_flush_missing_card(card1,card2,card3,card4):

    if card1[1]==card2[1] and card3[1]==card4[1] and card1[1]==card3[1]:
        
        color=card1[1]
        values=[get_value(card1[0]),get_value(card2[0]),get_value(card3[0]),get_value(card4[0])]
        values.sort()
        
        if abs(values[0]-values[3])==3:
            if values[3]+1<=14:
                return get_card(values[3]+1),color
            return get_card(values[3]-1),color
        
        if abs(values[0]-values[3])==4:
            for i in range(len(values)-1):
                if values[i]+1!=values[i+1]:
                    return get_card(values[i]+1),color

    return "No possible straight flush"


def get_value(card):
    value_table = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13,"A":14}
    return value_table[card]

def get_card(value):
    card_table = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    return card_table[value]


#You can obviously print these inside the function, but i personally to keep the code "print-free"
print(straight_flush_missing_card(["2","C"],["3","C"],["4","C"],["5","C"])) # --> ('8', 'C')
print(straight_flush_missing_card(["Q","P"],["9","P"],["7","P"],["6","P"])) # --> No possible straight flush
print(straight_flush_missing_card(["Q","P"],["K","P"],["9","P"],["10","P"])) # --> ('K', 'P')
