
import sys
import os


def count_lines(filename):
    count = 0

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            stripped = line.strip()

            if stripped == "":
                continue

            if stripped.startswith("#"):
                continue

            count += 1

    return count


def main():
    if len(sys.argv) != 2:
        print("Usage: python lines.py filename.py")
        sys.exit(1)

    filename = sys.argv[1]

    if not filename.endswith(".py"):
        print("Please provide a Python file.")
        sys.exit(1)

    if not os.path.isfile(filename):
        print("File does not exist.")
        sys.exit(1)

    try:
        print(count_lines(filename))

    except OSError as error:
        print(f"Error: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
