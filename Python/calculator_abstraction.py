from abc import ABC, abstractmethod


class Calculator(ABC):
    @abstractmethod
    def calculate(self, a, b):
        pass


class Addition(Calculator):
    def calculate(self, a, b):
        return a + b


class Subtraction(Calculator):

    def calculate(self, a, b):
        return a - b


class Multiplication(Calculator):

    def calculate(self, a, b):
        return a * b


class Division(Calculator):
    def calculate(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b


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


if __name__ == "__main__":
    add_calc = Addition()
    sub_calc = Subtraction()
    mul_calc = Multiplication()
    div_calc = Division()

    while True:
        choice = display_menu()

        if choice in ['1', '2', '3', '4']:
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")

            if choice == '1':
                print(f"Result: {num1} + {num2} = {add_calc.calculate(num1, num2)}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {sub_calc.calculate(num1, num2)}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {mul_calc.calculate(num1, num2)}")
            elif choice == '4':
                try:
                    result = div_calc.calculate(num1, num2)
                    print(f"Result: {num1} / {num2} = {result}")
                except ValueError as e:
                    print("Error:", e)

        elif choice == '5':
            print("Exiting the calculator.")
            break

        else:
            print("Invalid input. Please enter a valid option.")
