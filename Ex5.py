age=input("Enter your age");
if(age.isdigit()):
    age=int(age)
    if(age>=18):
        print("You are eligible for vote")
    elif(age<18):
        print("Not eligible for vote");
else:
    print("Invalid input");