from Calculator.BusinessLayer import MathFunctions

print("This is the Calculator v1.0")
number1: int(input("Enter the first number: "))
number2: int(input("Enter the second number: "))

print("Now , what would you like to do?")
print("1 - to Addition")
print("2 - to Substraction")
print("3 - to Multiply")
print("4 - to Divide")
option = int(input())

if(option==1):
    MathFunctions.addition(number1,number2)
elif(option==2):
    MathFunctions.minus(number1,number2)
elif(option==3):
    MathFunctions.multiplication(number1,number2)
elif(option==4):
    MathFunctions.division(number1,number2)


