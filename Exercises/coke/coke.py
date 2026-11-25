
def main():
    price = 50
    amount_paid = 0

    while amount_paid < price:
        print(f"Amount Due: {price - amount_paid}")

        try:
            coin = int(input("Insert Coin: "))

            if coin in [25, 10, 5]:
                amount_paid += coin
            else:
                print("Invalid coin. Insert 25, 10 or 5.")

        except ValueError:
            print("Please enter a valid coin.")

    print(f"Change Owed: {amount_paid - price}")


if __name__ == "__main__":
    main()
