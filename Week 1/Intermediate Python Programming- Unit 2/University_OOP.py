'''
Create a Python class to represent a University. The university should have
attributes like name, location, and a list of departments. Implement encapsulation to
protect the internal data of the University class. Create a Department class that
inherits from the University class. The Department class should have attributes like
department name, head of the department, and a list of courses offered. Implement
polymorphism by defining a common method for both the University and
Department classes to display their details.
'''

class University:
    """
    Represents a University with attributes like name, location, and departments.

    Attributes:
        name (str): The name of the university.
        location (str): The location of the university.
        departments (list): A list of department objects.
    """

    def __init__(self, name, location):
        self._name = name
        self._location = location
        self._departments = []

    def add_department(self, department):
        """
        Add a department to the university.

        Args:
            department (Department): The department object to add.
        """
        self._departments.append(department)

    def display_details(self):
        """
        Display the details of the university.
        """
        print(f"University Name: {self._name}")
        print(f"Location: {self._location}")
        print("Departments:")
        for department in self._departments:
            print(f"  - {department.get_name()}")


class Department(University):
    """
    Represents a Department within a university.

    Attributes:
        name (str): The name of the department.
        head_of_department (str): The head of the department.
        courses_offered (list): A list of courses offered by the department.
    """

    def __init__(self, name, head_of_department):
        super().__init__("Sample University", "Sample Location")
        self._name = name
        self._head_of_department = head_of_department
        self._courses_offered = []

    def add_course(self, course):
        """
        Add a course to the department.

        Args:
            course (str): The name of the course to add.
        """
        self._courses_offered.append(course)

    def get_name(self):
        """
        Get the name of the department.

        Returns:
            str: The name of the department.
        """
        return self._name

    def display_details(self):
        """
        Display the details of the department.
        """
        print(f"Department Name: {self._name}")
        print(f"Head of Department: {self._head_of_department}")
        print("Courses Offered:")
        for course in self._courses_offered:
            print(f"  - {course}")


# Example Usage:
if __name__ == "__main__":
    # Creating a University
    university = University("Tribhuwan University", "Kritipur")

    # Creating and adding departments to the University
    department1 = Department("Computer Science", "Sudeep Shakya")
    department1.add_course("Introduction to Programming")
    department1.add_course("Data Structures")
    department1.add_course("Applied mechanics")

    department2 = Department("Civil", "Firstname Lastname")
    department2.add_course("C Language")
    department2.add_course("Thermodynamics")
    department2.add_course("Transportation")

    university.add_department(department1)
    university.add_department(department2)

    # Displaying details of the University and its departments
    university.display_details()
    print()
    department1.display_details()
    print()
    department2.display_details()
