while True:
    choice = input('Type "Exit" to quit: ')
    if choice.lower() != "exit":
        x = float(input('Place your first number here: '))
        y = float(input('Place your second number here: '))
        operation = input('Choose to Add, Subtract, Multiply, or Divide: ')

        if operation.lower() == "add":
            print("Result:", x + y)
        elif operation.lower() == "subtract":
            print("Result:", x - y)
        elif operation.lower() == "multiply":
            print("Result:", x * y)
        elif operation.lower() == "divide":
            if y == 0:
                print("ERROR: Cannot divide by zero!")
            else:
                print("Result:", x / y)
        else:
            print("Invalid operation. Please choose Add, Subtract, Multiply, or Divide.")
    else:
        print("Exiting the program. Goodbye!")
        break
