# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   PSrianomai,8/17/2025,Created Script
# ------------------------------------------------------------------------------------------ #
import io as _io #needed to try closing in the finally block
import json #import code from Python's JSON module into my script


# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
menu_choice: str = ''  # Hold the choice made by the user.
students: list = []  # a table of student data

# Removed all of these and used them locally instead
# Define the Data Variables and constants
# student_first_name: str = ''  # Holds the first name of a student entered
# student_last_name: str = ''  # Holds the last name of a student entered
# course_name: str = ''  # Holds the name of a course entered by the user.
# student_data: dict = {}  # one row of student data
# file = None  # Holds a reference to an opened file.

# Processing---------------------------------------#
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    PSrianomai,8.17.2025,Created Class
    """

    # When the program starts, read the file data into a list of lists (table)
    # Extract the data from the file
    # When the program starts, the contents of the "Enrollments.json" are
    # automatically read into the students two-dimensional list of dictionary
    # rows using the json.load() function
    # read from the json file
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ This function reads student data from a file
        and returns it as a list of dictionaries.

        ChangeLog: (Who, When, What)
        PSrianomai,8/17.2025,Created function
        :return: list of student dictionaries
        """
        file = _io.TextIOWrapper # add file as a local variable
        try:  # use error handling
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running"
                                     " this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes student data to a file

        ChangeLog: (Who, When, What)
        PSrianomai,8/17.2025,Created function
        :return: None
        """
        file = _io.TextIOWrapper # add file as a local variable
        try:
            file = open(file_name, "w")
            json.dump(student_data, file, indent = 2) #write file using json dump
            file.close()
        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid "
                                     "JSON format", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()


# Presentation-------------------------------------#
class IO:
    """
    A collection of presentation layer functions that manage user input
    and output

    ChangeLog: (Who, When, What)
    PSrianomai,8.17.2025,Created Class
    PSrianomai,8.17.2025,Added menu output and input functions
    """
    @staticmethod
    def output_error_messages(message:str, error:Exception=None):
        """ This function displays the a custom error messages to the user

        ChangeLog: (Who, When, What)
        PSrianomai,8/17.2025,Created function
        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu:str):
        """ This function displays the a menu of choices to the user

        ChangeLog: (Who, When, What)
        PSrianomai,8.17.2025,Created function
        :return: None
        """
        print(menu)

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        PSrianomai,8.17.2025,Created function
        :return: string with the users choice
        """
        return input("Enter your menu choice number: ")

    @staticmethod
    def output_student_courses(student_data: list):
        """ This function displays the student courses

        ChangeLog: (Who, When, What)
        PSrianomai,8.17.2025,Created function
        :return: None
        """
        # Process the data to create and display a custom message
        print("-" * 50)
        for student in student_data:
            print(f'{student["FirstName"]},{student["LastName"]},'
                  f'{student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets the first name, last name, and
        course name from the user

        ChangeLog: (Who, When, What)
        PSrianomai,8.17.2025,Created function
        :return: student data (A dictionary containing 'FirstName',
        'LastName', and 'CourseName')
        """
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            #stores data input to student variable
            student = {"FirstName": student_first_name,
                       "LastName": student_last_name,
                       "CourseName": course_name}
            student_data.append(student)
            print(f"You have registered {student_first_name} "
                  f"{student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages("That value is not the "
                                     "correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        return student_data

#  End of function definitions

# Beginning of the main body of this script
students = FileProcessor.read_data_from_file(file_name = FILE_NAME,
                                             student_data = students)
# Repeat the follow tasks
while True:
    IO.output_menu(menu = MENU)

    menu_choice = IO.input_menu_choice()

    # On menu choice 1, the program prompts the user to enter the student's
    # first name and last name, followed by the course name, using the input()
    # function and stores the inputs in the respective variables.
    # Data collected for menu choice 1 is added to the students 2D list of
    # dictionaries rows.
    # using try-except to check when users input first names and last name
    if menu_choice == "1": # call input_student_data function
        students = IO.input_student_data(student_data=students)
        continue
    # Present the current data:
    # On menu choice 2, the presents a string by formatting the collected
    # data using the print() function.
    elif menu_choice == "2": # call output_student_courses function
        IO.output_student_courses(student_data=students)
        continue
    # On menu choice 3, the program opens a file named "Enrollments.json"
    # in write mode using the open() function. It writes the contents of
    # the students variable to the file using the json.dump() function.
    # Next, the file is closed using the close() method. Finally, the
    # program displays what was written to the file using the students variable
    elif menu_choice == "3":  # Call write_data_to_file function
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        # the program displays what was written to the file using the
        # students variable
        print("The following data was saved to file!")
        for student in students:
            print(f'{student["FirstName"]},{student["LastName"]},'
                  f'{student["CourseName"]}')
        continue

    # On menu choice 4, the program ends
    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3 or 4")

print("Program Ended")


