# calculator using function and if-else (beginner)

def add(x, y) -> float:
    return x + y


def sub(x, y) -> float:
    return x - y


def mul(x, y) -> float:
    return x * y


def div(x, y) -> float:
    return x / y


print(f"""
            The following are the operations:
            
            1. Addition
            2. Subtraction
            3. Multiplication
            4. Division
            5. Quit Calculator

""")

while True:

    choice = str(input("Enter Operation: "))

    if choice == "5":
        print("Exiting Calculator.")
        break

    num1 = float(input("Enter number: "))
    num2 = float(input("Enter number: "))

    if choice == "1":
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result:.2f}\n")

    elif choice == "2":
        result = sub(num1, num2)
        print(f"{num1} - {num2} = {result:.2f}\n")

    elif choice == "3":
        result = mul(num1, num2)
        print(f"{num1} * {num2} = {result:.2f}\n")

    elif choice == "4":
        result = div(num1, num2)
        print(f"{num1} / {num2} = {result:.2f}\n")

    else:
        print("Invalid Operation.")


