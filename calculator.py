import math
def addtion():
    n1=int(input("Enter the 1st number: "))
    n2=int(input("Enter the 2nd number: "))
    sum=n1+n2
    print("The sum is : ",sum)

def sqrt():
    n=int(input("Enter a number\n"))
    s=math.sqrt(n)
    print("Square root of ",n," is ",s)
<<<<<<< HEAD
def multiplication():
    n1=int(input("Enter the 1st number: "))
    n2=int(input("Enter the 2nd number: "))
    mul=n1+n2
    print("The multiplication is : ",mul)

=======
def div():
    n1=int(input("Enter the 1st number: "))
    n2=int(input("Enter the 2nd number: "))
    d=n1/n2
    print("The sum is : ",d)
>>>>>>> eb3528de1269177ede4dcc7828517864668a7073
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
            multiplication()
        case 4:
            div()
        case 5:
            sqrt()
        case 6:
            print("Work In Progress")
        case 7:
            print("Thank You!")
        case default:
            print("Enter a valid option..")
            op=0