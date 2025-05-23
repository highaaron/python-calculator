while True:
    try:
        number1 = float(input("Number 1: "))
        number2 = float(input("Number 2: "))

        print("\nChoose an operation:")
        print("A for Addition")
        print("S for Subtraction")
        print("M for Multiplication")
        print("D for Division")
        print("R for Modulo (Remainder)")
        print("Q to Quit")

        choice = input("Your choice: ").upper()

        if choice == "A":
            result = number1 + number2
            print("Result =", round(result, 2))
        elif choice == "S":
            result = number1 - number2
            print("Result =", round(result, 2))
        elif choice == "M":
            result = number1 * number2
            print("Result =", round(result, 2))
        elif choice == "D":
            if number2 == 0:
                print("🚫 Can't divide by zero.")
            else:
                result = number1 / number2
                print("Result =", round(result, 2))
        elif choice == "R":
            if number2 == 0:
                print("🚫 Can't modulo by zero.")
            else:
                result = number1 % number2
                print("Remainder =", round(result, 2))
        elif choice == "Q":
            print("🛑 Quitting the calculator. Bye!")
            break
        else:
            print("❌ Invalid input. Try again.")

        print("-" * 40)

    except ValueError:
        print("⚠️ Please enter a valid number.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")
