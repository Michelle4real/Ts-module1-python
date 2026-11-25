
def main():
    while True:
        try:
            fraction = input("Fraction: ")
            numerator, denominator = fraction.split("/")

            numerator = int(numerator)
            denominator = int(denominator)

            if denominator == 0:
                raise ValueError

            if numerator < 0 or numerator > denominator:
                raise ValueError

            percentage = round(numerator / denominator * 100)

            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")

            break

        except (ValueError, ZeroDivisionError):
            print("Invalid fraction. Try again.")


if __name__ == "__main__":
    main()
