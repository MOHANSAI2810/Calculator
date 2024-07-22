a=int(input("Enter first number"))
b=int(input("Enter second number"))
print("Enter your choioce")
c=int(input("1.Addition\n2.Substration\n3.Multiplication\n4.Division\n"))
if c==1:
    d=a+b
    print("The sum of",a,"and",b,"is",d)
elif c==2:
    d=a-b
    print("The differnce of",a,"and",b,"is",d)
elif c==3:
    d=a*b
    print("The product of",a,"and",b,"is",d)
elif c==4:
    if b==0:
        try:
            d=a/b
        except ZeroDivisionError:
            print("Dision with zero not possible")
    else:
        d=a/b
        print("The division of",a,"and",b,"is",d)
else:
    print("Select among 1-4 only")