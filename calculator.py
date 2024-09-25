def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def get_user_input():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

def main():
    while True:
        print("Choose an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            num1, num2 = get_user_input()
            result = add(num1, num2)
            print("Result:", result)
        elif choice == '2':
            num1, num2 = get_user_input()
            result = subtract(num1, num2)
            print("Result:", result)
        elif choice == '3':
            num1, num2 = get_user_input()
            result = multiply(num1, num2)
            print("Result:", result)
        elif choice == '4':
            num1, num2 = get_user_input()
            result = divide(num1, num2)
            print("Result:", result)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
