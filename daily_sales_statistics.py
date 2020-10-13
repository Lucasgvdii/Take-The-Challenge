#The daily sales statistics problem. Link to the explanation and heading of the problem --> https://www.aceptaelreto.com/problem/statement.php?id=108

#Main function
def daily_sales_statistics(daily_sales_list):
    
    statistics=""

    lunch_sale=0
    
    total_v_sales=0
    
    min_meal=""
    min_meal_sale=0
    max_meal=""
    max_meal_sale=0
    
    for i in daily_sales_list:
        if i[1]<min_meal_sale:
            min_meal_sale=i[1]
            min_meal=i[0]
        elif i[1]==min_meal_sale:
            min_meal=min_meal+i[0]
        elif i[1]==max_meal_sale:
            max_meal=max_meal+i[0]
        elif i[1]>max_meal_sale:
            max_meal_sale=i[1]
            max_meal=i[0]

        if i[0]=="A":
            lunch_sale=i[1]

    total_v_sales=total_v_sales+i[1]

    avg_sales=total_v_sales/5
    statistics=statistics+get_day(max_meal)+get_day(min_meal)
    if avg_sales<lunch_sale:
        statistics=statistics+"Yes"
    else:
        statistics=statistics+"No"
            
    return statistics
                

def get_day(day):
    if day=="D":
        return "breakfast#"
    elif day=="A":
        return "lunch#"
    elif day=="M":
        return "snack#"
    elif day=="I":
        return "dinner#"
    elif day=="C":
        return "cocktails#"
    else:
        return "tie#"
                
        
#You can obviously print these inside the function, but i personally like to keep the code "print-free"
print(daily_sales_statistics([["D",2.8],["C",48.0],["A",8.0],["N",0]]))                  # --> cocktails#tie#No
print(daily_sales_statistics([["D",15.33],["A",60.0],["M",12.0],["I",25.0],["N",0]]))    # --> lunch#tie#Yes
