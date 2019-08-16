import option as option
from Calculator.BusinessLayer import MathFunctions
from Calculator.BusinessLayer import MainFunctions
from Calculator.BusinessLayer.MainFunctions import menu, enterNumber

number1=0
number2=0
option=0

number1,number2 = enterNumber(number1,number2)
option=menu(option)
print(number1,number2,option)

if(option==1):
    MathFunctions.addition(number1,number2)
elif(option==2):
    MathFunctions.minus(number1,number2)
elif(option==3):
    MathFunctions.multiplication(number1,number2)
elif(option==4):
    MathFunctions.division(number1,number2)
else:
    print("Wrong option!")
    print("Do you want to do another thing?")
    print("Y - Yes")
    print("N - No")
    choice = input()

    if (choice == 'Y'):
        number1,number2 = enterNumber(number1, number2)
        option = menu(option)
    elif (choice == 'N'):
        print("Thank you")


print("Do you want to do another thing?")
print("Y - Yes")
print("N - No")
choice = input()

if(choice=='Y'):
    enterNumber(number1,number2)
    menu(option)
elif(choice=='N'):
    print("Thank you")
