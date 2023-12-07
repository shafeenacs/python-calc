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

def multiplication():
    n1=int(input("Enter the 1st number: "))
    n2=int(input("Enter the 2nd number: "))
    mul=n1+n2
    print("The multiplication is : ",mul)

def div():
    n1=int(input("Enter the 1st number: "))
    n2=int(input("Enter the 2nd number: "))
    d=n1/n2

    print("The sum is : ",d)

def subtraction():
    a=int(input("Enter 1st number"))
    b=int(input("Enter 2nd number"))
    d=a-b
    print("Difference = ",d)
    return
def power():
    a=int(input("Enter the base"))
    b=int(input("Enter the exponent"))
    res=pow(a,b)
    print("Power = ",res)
    return
 



print("1.Addition\n2.Substraction\n3.Multiplication\n4.Division\n5.Square-Root\n6.Power\n7.exit\n")
op=0
while op<7:
    op=int(input("Enter Your Option!\n"))
    match op:
        case 1:
            addtion()
        case 2:
            subtraction()
        case 3:
            multiplication()
        case 4:
            div()
        case 5:
            sqrt()
        case 6:
            power()
        case 7:
            print("Thank You!")
        case default:
            print("Enter a valid option..")
            op=0
