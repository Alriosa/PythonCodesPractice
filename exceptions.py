




def divide():
    print("Division, enter two numbers")

    number1 = int(input("Number 1: "))
    number2 = int(input("Number 2: "))
    try:
        return number1/number2
    except ZeroDivisionError:
        print("Error, You can't make a division with a cero")
    except ValueError:
        print("Error, Wrong value entered")

divide()