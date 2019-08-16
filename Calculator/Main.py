import option as option
from Calculator.BusinessLayer import MathFunctions
from Calculator.BusinessLayer import MainFunctions
from Calculator.BusinessLayer.MainFunctions import menu, enterNumber, Calculate

number1=0
number2=0
option=0
choice=""

number1,number2 = enterNumber(number1,number2)
option=menu(option)
print(number1,number2,option)

Calculate(number1,number2,option)



