hour = 0
goal_sum = 0
store = False
print ("The 8 hours working day is started")
while hour !=8:
    hour +=1
    print (hour, "hour")
    resolved_goals = int (input ("How many goals does Maxim resolve?"))
    goal_sum += resolved_goals
    
    call = int (input ("The wife is calling. Take the phone? (1 - yes, 0 -no)"))
    if call == 1:
        store = True
print ("The working day is complete. Goals were made in total:", goal_sum)
if store:
    print ("It is due to shopping")