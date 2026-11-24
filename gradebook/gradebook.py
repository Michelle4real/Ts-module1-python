import csv
import sys
import os
import statistics


def letter(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def load_students(filename):
    students = []

    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        required_columns = {"name", "course", "score"}

        if not required_columns.issubset(reader.fieldnames or []):
            raise ValueError("CSV must contain name, course and score columns.")

        for row in reader:
            try:
                score = float(row["score"])

                student = {
                    "name": row["name"],
                    "course": row["course"],
                    "score": score,
                    "grade": letter(score)
                }

                students.append(student)

            except (ValueError, TypeError):
                print(
                    f"Warning: Skipping invalid score "
                    f"for {row.get('name', 'unknown student')}."
                )

    return students


def print_summary(students):
    if not students:
        print("No valid student scores found.")
        return

    scores = [student["score"] for student in students]

    print(f"Students: {len(students)}")
    print(f"Mean: {statistics.mean(scores):.1f}")
    print(f"Median: {statistics.median(scores):.1f}")

    highest = max(students, key=lambda student: student["score"])
    lowest = min(students, key=lambda student: student["score"])

    print(f"Highest: {highest['name']} ({highest['score']:g})")
    print(f"Lowest: {lowest['name']} ({lowest['score']:g})")


def write_report(students):
    sorted_students = sorted(
        students,
        key=lambda student: student["score"],
        reverse=True
    )

    with open("report.txt", "w", encoding="utf-8") as file:
        for student in sorted_students:
            file.write(
                f"{student['name']},"
                f"{student['score']:g},"
                f"{student['grade']}\n"
            )

    print("Report saved to report.txt")


def main():
    if len(sys.argv) == 1:
        print("Error: Please provide a CSV filename.")
        sys.exit(1)

    if len(sys.argv) > 2:
        print("Error: Too many arguments.")
        sys.exit(1)

    filename = sys.argv[1]

    if not filename.lower().endswith(".csv"):
        print("Error: File must have a .csv extension.")
        sys.exit(1)

    if not os.path.isfile(filename):
        print("Error: File does not exist.")
        sys.exit(1)

    try:
        students = load_students(filename)

        print_summary(students)
        write_report(students)

    except (OSError, csv.Error, ValueError) as error:
        print(f"Error: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()