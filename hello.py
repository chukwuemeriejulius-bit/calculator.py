while True:
    operator = input(" choose operator (+, -, *, /, ) or q, to quite:").strip()
    if operator.lower() == "q":
        print("caculator, closed.")
        break
    if operator not in ["+", "-", "/", "*"]:
        print("invalid operator.")
        continue
    try:
        first = float(input("first number:"))
        second = float(input("second number:"))
    except ValueError:
        print("enter a valid number:")
        continue
    if operator == "+":
        result = first + second
    elif operator == "-":
        result = first - second
    elif operator == "*":
        result = first * second
    elif operator == "/":
        if second == 0:
            print("cannot divide by zero !")
            continue
        result = first / second
        print(f"result: {result}")
