exp = input("Expression: ")

x, y, z = exp.split()

match y:
    case "+":
        print(f"{(float(x) + float(z)):.1f}")

    case "-":
        print(f"{(float(x) - float(z)):.1f}")

    case "*":
        print(f"{(float(x) * float(z)):.1f}")

    case "/":
        print(f"{(float(x) / float(z)):.1f}")

    case _:
        print("Enter a valid expression")


