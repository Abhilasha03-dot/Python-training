print("Welcome to events")
name=input("Enter your name:")
choice=int(input("Select Event : 1.Sport 2.Concert"))
if choice == 1:
    print(" Please come at ground sharp 11am")
    age=int(input("Enter your age:"))
    if age>18:
        print("Go to section A")
    elif age<18:
        print("Go to section B")
    else:
        print("Go to home")
        
    
elif choice == 2:
    print("Please come at Dj house at 7pm")
else:
     print("Do not come sleep at home")
print(f"Thank you {name}")