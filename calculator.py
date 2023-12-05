def addtion():
    n1=int(input("Enter the 1st number: "))
    n2=int(input("Enter the 2nd number: "))
    sum=n1+n2
    print("The sum is : ",sum)

print("1.Addition\n2.Substraction\n3.Multiplication\n4.Division\n5.Square-Root\n6.Power\n7.exit\n")
op=0
while op<7:
    op=int(input("Enter Your Option!\n"))
    match op:
        case 1:
            addtion()
        case 2:
            print("Work In Progress")
        case 3:
            print("Work In Progress")
        case 4:
            print("Work In Progress")
        case 5:
            print("Work In Progress")
        case 6:
            print("Work In Progress")
        case default:
            print("Enter a valid option..")