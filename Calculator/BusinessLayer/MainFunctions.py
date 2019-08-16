from Calculator.BusinessLayer import MathFunctions


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


def Calculate(number1,number2,option):
    if (option == 1):
        MathFunctions.addition(number1, number2)
        print("Do you want to do another thing?")
        print("Y - Yes")
        print("N - No")
        choice = input()

        if (choice == 'Y'):
            enterNumber(number1, number2)
            menu(option)
            Calculate(number1, number2, option)
        elif (choice == 'N'):
            print("Thank you")
    elif (option == 2):
        MathFunctions.minus(number1, number2)
        print("Do you want to do another thing?")
        print("Y - Yes")
        print("N - No")
        choice = input()

        if (choice == 'Y'):
            enterNumber(number1, number2)
            menu(option)
            Calculate(number1, number2, option)
        elif (choice == 'N'):
            print("Thank you")
    elif (option == 3):
        MathFunctions.multiplication(number1, number2)
        print("Do you want to do another thing?")
        print("Y - Yes")
        print("N - No")
        choice = input()

        if (choice == 'Y'):
            enterNumber(number1, number2)
            menu(option)
            Calculate(number1, number2, option)
        elif (choice == 'N'):
            print("Thank you")
    elif (option == 4):
        MathFunctions.division(number1, number2)
        print("Do you want to do another thing?")
        print("Y - Yes")
        print("N - No")
        choice = input()

        if (choice == 'Y'):
            enterNumber(number1, number2)
            menu(option)
            Calculate(number1, number2, option)
        elif (choice == 'N'):
            print("Thank you")
    else:
        print("Wrong option!")
        print("Do you want to do another thing?")
        print("Y - Yes")
        print("N - No")
        choice = input()

        if (choice == 'Y'):
            number1, number2 = enterNumber(number1, number2)
            option = menu(option)
            print("Do you want to do another thing?")
            print("Y - Yes")
            print("N - No")
            choice = input()

            if (choice == 'Y'):
                enterNumber(number1, number2)
                menu(option)
                Calculate(number1, number2, option)
            elif (choice == 'N'):
                print("Thank you")
        elif (choice == 'N'):
            print("Thank you")