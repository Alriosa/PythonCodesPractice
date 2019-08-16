def menu(option):
    print("Now , what would you like to do?")
    print("1 - to Addition")
    print("2 - to Substraction")
    print("3 - to Multiply")
    print("4 - to Divide")
    option = int(input())

    return option

def enterNumber(number1,number2):
    print("This is the Calculator v1.0")
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    return number1,number2