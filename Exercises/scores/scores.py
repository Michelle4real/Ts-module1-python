
import csv
import statistics
import sys
import os


def load_scores(filename):
    students = []

    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        if not {"name", "score"}.issubset(reader.fieldnames or []):
            raise ValueError("CSV must contain name and score columns.")

        for row in reader:
            try:
                name = row["name"].strip()
                score = float(row["score"])

                if not name or not 0 <= score <= 100:
                    print("Skipping invalid student record.")
                    continue

                students.append({
                    "name": name,
                    "score": score
                })

            except (ValueError, TypeError):
                print("Skipping invalid score.")

    return students


def print_results(students):
    if not students:
        print("No valid scores found.")
        return

    scores = [student["score"] for student in students]

    top = max(students, key=lambda student: student["score"])
    bottom = min(students, key=lambda student: student["score"])

    print(f"Mean: {statistics.mean(scores):.2f}")
    print(f"Median: {statistics.median(scores):.2f}")
    print(f"Top student: {top['name']} ({top['score']:g})")
    print(f"Bottom student: {bottom['name']} ({bottom['score']:g})")


def main():
    filename = "scores.csv"

    if not os.path.isfile(filename):
        print("Error: scores.csv does not exist.")
        sys.exit(1)

    try:
        students = load_scores(filename)
        print_results(students)

    except (OSError, csv.Error, ValueError) as error:
        print(f"Error: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
