age=input("Enter your age");
if(age.isdigit()):
    age=int(age)
    if(age<18):
        print("Child")
    elif(age>=18 & age <35):
        print("Youth")
    elif(age>=35 & age <60):
        print("Citizen")
    elif(age>=60):
        print("Seniour Citizen")
else:
    print("Invalid input")

