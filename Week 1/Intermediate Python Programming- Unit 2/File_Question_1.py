'''
Question 1 - file
Implement a program that reads a CSV file named "data.csv," containing columns
"Name" and "Age." Create a new CSV file called "adults.csv" with only the rows of
individuals who are 18 years or older.
'''


import csv

def filter_adults(input_filename, output_filename):
    """
    Read a CSV file containing "Name" and "Age" columns and create a new CSV file with
    only the rows of individuals who are 18 years or older.

    Args:
        input_filename (str): The name of the input CSV file.
        output_filename (str): The name of the output CSV file.

    Returns:
        None

    """
    try:
        with open(input_filename, 'r', newline='') as input_file, open(output_filename, 'w', newline='') as output_file:
            reader = csv.DictReader(input_file)
            fieldnames = reader.fieldnames
            writer = csv.DictWriter(output_file, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                age = int(row['Age'])
                if age >= 18:
                    writer.writerow(row)
    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
    except ValueError:
        print(f"Error: Invalid data in the file '{input_filename}'.")

if __name__ == "__main__":
    input_filename = "data.csv"
    output_filename = "adults.csv"

    filter_adults(input_filename, output_filename)
