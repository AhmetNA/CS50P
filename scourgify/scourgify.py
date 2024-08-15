import csv 
import sys

def take_args():
    if len(sys.argv) < 3:
        print("Too few arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many arguments")
        sys.exit(1)
    return sys.argv[1], sys.argv[2]

def main():
    before, after = take_args()
    if before != "before.csv":
        print("Invalid input file")
        sys.exit(1)

    with open(before, "r", newline='') as before_file:
        before_read = csv.DictReader(before_file)

        # Check if the format of the input CSV is correct
        if before_read.fieldnames != ["name", "house"]:
            print("Invalid format")
            sys.exit(1)

        with open(after, "w", newline='') as after_file:
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(after_file, fieldnames=fieldnames)
            writer.writeheader()

            # Process each row and write the new format
            for row in before_read:
                last, first = row["name"].split(", ")
                house = row["house"]
                writer.writerow({
                    "first": first.strip(),
                    "last": last.strip(),
                    "house": house.strip()
                })

if __name__ == "__main__":
    main()
