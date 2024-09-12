# calculator using encapsulation
class Calculator:

    def __init__(self):
        self.result = 0

    def add(self, a, b):
        self.result = a + b
        return self.result

    def subtract(self, a, b):
        self.result = a - b
        return self.result

    def multiply(self, a, b):
        self.result = a * b
        return self.result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        self.result = a / b
        return self.result

    def get_result(self):
        return self.result

    def clear(self):
        self.result = 0


# Function to display menu and take user input
def display_menu():
    print("\nSimple Calculator")
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Clear")
    print("6. Exit")

    choice = input("Enter choice (1/2/3/4/5/6): ")
    return choice


# Main program to interact with the user
if __name__ == "__main__":
    calc = Calculator()

    while True:
        choice = display_menu()

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if choice == '1':
                    print(f"Result: {num1} + {num2} = {calc.add(num1, num2)}")
                elif choice == '2':
                    print(f"Result: {num1} - {num2} = {calc.subtract(num1, num2)}")
                elif choice == '3':
                    print(f"Result: {num1} * {num2} = {calc.multiply(num1, num2)}")
                elif choice == '4':
                    print(f"Result: {num1} / {num2} = {calc.divide(num1, num2)}")
            except ValueError as e:
                print("Error:", e)

        elif choice == '5':
            calc.clear()
            print("Calculator reset.")

        elif choice == '6':
            print("Exiting the calculator.")
            break

        else:
            print("Invalid input. Please enter a valid option.")