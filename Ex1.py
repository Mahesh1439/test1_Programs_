num=input("Enter any number: ");
if num.isdigit():
   num=int(num)
   if num>0:
    print("Positive number")
   elif(num<0):
        print("Negative number")   
   elif(num==0):
        print("You entered zero") 
else:
    print("Invalid num")