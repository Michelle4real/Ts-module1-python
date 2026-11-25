
def main():
    while True:
        try:
            meal = float(
                input("How much was the meal? ").replace("$", "")
            )
            percentage = float(
                input("What percentage would you like to tip? ")
                .replace("%", "")
            )

            if meal < 0 or percentage < 0:
                print("Please enter positive amounts.")
                continue

            tip = meal * percentage / 100

            print(f"Leave ${tip:.2f}")
            break

        except ValueError:
            print("Please enter valid numbers.")


if __name__ == "__main__":
    main()
