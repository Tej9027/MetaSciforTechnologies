class Calculator:
    def __init__(self):
        self.result = 0  # Protected variable to store the result

    def get_result(self):
        return self.result


class Addition(Calculator):
    def add(self, a, b):
        self.result = a + b
        return self.result


class Subtraction(Calculator):
    def subtract(self, a, b):
        self.result = a - b
        return self.result


class Multiplication(Calculator):
    def multiply(self, a, b):
        self.result = a * b
        return self.result


class Division(Calculator):
    def __init__(self):
        super().__init__()
        self.result = None

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        self.result = a / b
        return self.result


# Function to display menu and take user input
def display_menu():
    print("\nSimple Calculator")
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")
    return choice


# Function to get a valid float input from the user
def get_number(prompt):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Main program to interact with the user
if __name__ == "__main__":
    # Create instances of each operation class
    add_calc = Addition()
    sub_calc = Subtraction()
    mul_calc = Multiplication()
    div_calc = Division()

    while True:
        choice = display_menu()

        if choice in ['1', '2', '3', '4']:
            # Get the first and second numbers from the user
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")

            # Perform the selected operation using inheritance
            if choice == '1':
                print(f"Result: {num1} + {num2} = {add_calc.add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {sub_calc.subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {mul_calc.multiply(num1, num2)}")
            elif choice == '4':
                try:
                    result = div_calc.divide(num1, num2)
                    print(f"Result: {num1} / {num2} = {result}")
                except ValueError as e:
                    print("Error:", e)

        elif choice == '5':
            print("Exiting the calculator.")
            break

        else:
            print("Invalid input. Please enter a valid option.")
