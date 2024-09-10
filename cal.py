num1=int(input("Enter 1st int: "))
num2=int(input("Enter 2nd int: "))
op=input("Enter the arithmatic oparetors [+,-,*,/,%]:")
if op == '+':
    result=num1+num2
elif op=='-':
    result=num1-num2 
elif op=='*':
    result=num1*num2
elif op=='/':
    result=num1 / num2
elif op=='%':
    result=num1 % num2
else:
    print("Oparetor is wrong . Program will blast now.")
print(num1,op,num2,"=", result)
