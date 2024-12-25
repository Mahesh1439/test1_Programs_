num=input("Enter a number")
if num.isdigit():
   num=int(num)
   if(num%5==0):
        print("Vegetarian")
   elif(num%10==0):
        print("Non Veg")
   elif(num%5==0 & num%10==0):
       print("Vegan")
else:
    print("Invalid input")