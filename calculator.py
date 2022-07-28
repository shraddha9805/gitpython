while True:
    print("menu driven program")
    print("addition")
    print("substraction")
    print("division")
    print("multiplication")
    choice=int(input("enter your choice"))
    if choice == 1:
        num1=int(input ("enter the num1"))
        num2=int(input ("enter the num2"))
        ans =num1+num2
        print(f"additon {ans} ")
    elif choice == 2:
        num1=int(input ("enter the num1"))
        num2=int(input ("enter the num2"))
        ans =num1-num2
        print(f"subtration {ans} ")
    elif choice == 3:
        num1=int(input ("enter the num1"))
        num2=int(input ("enter the num2"))
        ans =num1*num2
        print(f"multiplication {ans} ")
    elif choice == 4:
        num1=int(input ("enter the num1"))
        num2=int(input ("enter the num2"))
        ans =num1/num2
        print(f"divsion {ans} ")
    elif choice == 5:
        num1=int(input ("enter the num1"))
        num2=int(input ("enter the num2"))
        ans =num1%num2
        print(f"modulus {ans} ")
    elif choice == 6:
        break
    else:
        print("please  entercorrect choice")
    