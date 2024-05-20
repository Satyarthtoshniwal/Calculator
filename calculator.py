
#calculator
num1=input("Enter first number:\n")
operator=input("Enter the operator among +,-,*,/,%\n")
num2=input("Enter second number:\n")
num1=int(num1)
num2=int(num2)
if operator == "+":
    sum=(num1+num2)
    print(str(num1) + "+" + str(num2) + "=" + str(sum))
elif operator=="-":
    sum=(num1-num2)
    print(str(num1) + "-" + str(num2) + "=" + str(sum))
elif operator =="*":
    sum=(num1*num2)
    print(str(num1) + "*" + str(num2) + "=" + str(sum))
elif operator=="/":
    sum=(num1/num2)
    print(str(num1) + "/" + str(num2) + "=" + str(sum))
elif operator=="%":
    sum=(num1%num2)
    print(str(num1) + "%" + str(num2) + "=" + str(sum))
else:
    print("invalid operator")