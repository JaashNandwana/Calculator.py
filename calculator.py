def calculator():
    print("Welcome to the Calculator!")
    print("Select an operation to perform:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        try:
            # Get user choice
            choice = input("Enter choice (1/2/3/4): ")

            # Check if the choice is valid
            if choice not in ('1', '2', '3', '4'):
                print("Invalid input. Please enter a number between 1 and 4.")
                continue

            # Get numbers from the user
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            # Perform the selected operation
            if choice == '1':
                print(f"The result of {num1} + {num2} is {num1 + num2}")
            elif choice == '2':
                print(f"The result of {num1} - {num2} is {num1 - num2}")
            elif choice == '3':
                print(f"The result of {num1} * {num2} is {num1 * num2}")
            elif choice == '4':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    print(f"The result of {num1} / {num2} is {num1 / num2}")

            # Ask if the user wants to perform another calculation
            next_calculation = input("Would you like to perform another calculation? (yes/no): ").lower()
            if next_calculation != 'yes':
                print("Thank you for using the calculator! Goodbye!")
                break
        except ValueError:
            print("Invalid input. Please enter numeric values.")

# Run the calculator function
calculator()
