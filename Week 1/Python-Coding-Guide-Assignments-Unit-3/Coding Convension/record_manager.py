'''
Create a Python program that manages student records. The program should have the
following functionalities:
- Create a function that can add new students to the records with their student_id,
name, age, and grade. The records should be saved to “json” file and each time
new record is added, it should be saved to same “json” file
- Allow searching for a student by student_id or name. The data should return age
and grade from the saved file.
- Allow updating a student's information by using student_id or name(age or grade)
Ensure to follow PEP8 Coding Guidelines for following criterias:
- Proper Indentation
- Maximum Line Length
- Prescriptive Naming conventions (Package and Module Names, Class Names,
Exception Names, Global Variable Names, Function and Variable Names, Method
Names and Instance Variables, Constants)
- Source File Encoding while accessing the JSON file
- Add NumPy Docstring to each function
'''


import json

class StudentRecordManager:
    """
    Class for managing student records.

    This class provides functionality to add, search, and update student records.
    Records are saved to a JSON file.
    """

    def __init__(self, file_name):
        """
        Initialize the StudentRecordManager.

        Args:
            file_name (str): Name of the JSON file to save records.
        """
        self.file_name = file_name
        self.records = self._load_records()

    def _load_records(self):
        """
        Load student records from the JSON file.

        Returns:
            dict: Loaded records from the JSON file.
        """
        try:
            with open(self.file_name, 'r', encoding='utf-8') as file:
                records = json.load(file)
            return records
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def _save_records(self):
        """
        Save student records to the JSON file.
        """
        with open(self.file_name, 'w', encoding='utf-8') as file:
            json.dump(self.records, file, indent=4)

    def add_student(self, student_id, name, age, grade):
        """
        Add a new student record to the records.

        Args:
            student_id (int): Student ID.
            name (str): Student name.
            age (int): Student age.
            grade (str): Student grade.

        Returns:
            dict: Added student record.
        """
        student = {
            'student_id': student_id,
            'name': name,
            'age': age,
            'grade': grade
        }
        self.records[student_id] = student
        self._save_records()
        return student

    def search_student(self, key):
        """
        Search for a student record by student_id or name.

        Args:
            key (int or str): Student ID or name to search for.

        Returns:
            dict or None: Student record if found, None otherwise.
        """
        for student in self.records.values():
            if key == student['student_id'] or key == student['name']:
                return {'age': student['age'], 'grade': student['grade']}
        return None

    def update_student(self, key, attribute, new_value):
        """
        Update a student's information by student_id or name.

        Args:
            key (int or str): Student ID or name to update.
            attribute (str): Attribute to update ('age' or 'grade').
            new_value: New value for the attribute.

        Returns:
            bool: True if update was successful, False otherwise.
        """
        for student in self.records.values():
            if key == student['student_id'] or key == student['name']:
                student[attribute] = new_value
                self._save_records()
                return True
        return False

# Demonstrate the StudentRecordManager in action
if __name__ == "__main__":
    manager = StudentRecordManager("student_records.json")

    while True:
        print("\nStudent Record Management")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Update Student Info")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_id = int(input("Enter Student ID: "))
            name = input("Enter Student Name: ")
            age = int(input("Enter Student Age: "))
            grade = input("Enter Student Grade: ")
            manager.add_student(student_id, name, age, grade)
            print("Student added successfully!")

        elif choice == "2":
            key = input("Enter Student ID or Name to search: ")
            result = manager.search_student(key)
            if result:
                print("Student found:")
                print(f"Age: {result['age']}, Grade: {result['grade']}")
            else:
                print("Student not found.")

        elif choice == "3":
            key = input("Enter Student ID or Name to update: ")
            attribute = input("Enter attribute to update (age or grade): ")
            new_value = input("Enter new value: ")
            if manager.update_student(key, attribute, new_value):
                print("Student information updated successfully!")
            else:
                print("Student not found.")

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please select a valid option.")
