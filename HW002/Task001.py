rating = int(input("Enter the num: "))
positive_count = 0
negative_count = 0
while rating !=0:
    if rating > 0:
        positive_count +=1
    else:
        negative_count +=1
rating = int(input("Enter the num: "))
print ("The ammount of positive nums: ", positive_count)   
print ("The amount of negative nums: ", negative_count)     