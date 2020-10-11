#The selling statistisc problem. Link to the explanation of the problem --> https://www.aceptaelreto.com/problem/statement.php?id=105

#Main function
def statistics_viewer(weeks):
    week_days=["Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    result=[]
    for i in range(len(weeks)):
        if i%6==0:
            min_selling_day=i%6
            min_selling_inc=weeks[i]

            max_selling_day=i%6
            max_selling_inc=weeks[i]
            
            total_week_inc=weeks[i]
            
        else:
            if min_selling_inc>weeks[i]:
                min_selling_day=i%6
                min_selling_inc=weeks[i]

            if max_selling_inc<weeks[i]:
                max_selling_day=i%6
                max_selling_inc=weeks[i]

            total_week_inc=total_week_inc+weeks[i]
   
            if  i%6==5:
                sunday_higher_than_avg="NO"
                if total_week_inc/6<weeks[i]:
                    sunday_higher_than_avg="YES"
                    
                result.append([week_days[max_selling_day],week_days[min_selling_day],sunday_higher_than_avg])

    return result        

#You can obviously print these inside the function, but i personally like to keep the code "print-free"
print(statistics_viewer([185.50,250.36,163.45,535.20,950.22,450.38]))                        # --> [['Thursday', 'Saturday', 'YES']]
print(statistics_viewer([15.50,25.36,63.5,55.0,90.22,0.38,34.2,13.4,56.8,76.2,2.9,24.3]))    # --> [['Saturday', 'Sunday', 'NO'], ['Friday', 'Saturday', 'NO']]
