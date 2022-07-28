area=int(input("enter your choice "))
match area:
    case 1:
        def circle(R):
            pi=3.14
            print(f"area of circle {pi*R*R}")
        if __name__ == "__main__":
              radius=float(input("enter the radius:"))
              circle(radius)
    case 2:
        def square(s):
            print(f"area of square{s*s}")
        if __name__ == "__main__":
              side=int(input("enter the side:"))
              square(side)
    case 3:
        def rectangle(l,b):
            print(f"area of rectangle{l*b}")
        if __name__ == "__main__":
              length=int(input("enter the length:"))
              breadth=int(input("enter the length:"))
              rectangle(length,breadth)    
    case 4:
        print("please enter correct choice")       

