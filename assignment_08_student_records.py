# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
# TASK: Student Record Management System

students = []  # this will hold all our student dictionaries


def add_student():
    name = input("Student name: ")
    student_id = int(input("Student ID: "))

    num_scores = int(input("How many scores? "))
    scores = []

    for i in range(num_scores):
        score = int(input("Enter score " + str(i + 1) + ": "))
        scores.append(score)

    # build the dictionary for this student
    new_student = {
        "name": name,
        "id": student_id,
        "scores": scores
    }

    students.append(new_student)
    print("Student \"" + name + "\" added successfully.")


def get_average(scores):
    # add everything up then divide, nothing fancy
    total = 0
    for s in scores:
        total = total + s

    avg = total / len(scores)
    return round(avg, 2)


def display_all_students():
    if len(students) == 0:
        print("No students have been added yet.")
        return

    print("-" * 50)
    print("Name           ID          Scores         Average")
    print("-" * 50)

    for student in students:
        scores_text = ""
        for i in range(len(student["scores"])):
            scores_text += str(student["scores"][i])
            if i != len(student["scores"]) - 1:
                scores_text += ", "

        avg = get_average(student["scores"])

        print("{:<15}{:<12}{:<15}{}".format(
            student["name"], student["id"], scores_text, avg
        ))

    print("-" * 50)


def find_average_by_id():
    search_id = int(input("Enter student ID: "))
    found = False

    for student in students:
        if student["id"] == search_id:
            avg = get_average(student["scores"])
            print(student["name"] + "'s average score: " + str(avg))
            found = True
            break

    if not found:
        print("Error: no student found with that ID.")


def show_menu():
    print("================================")
    print("   STUDENT RECORD SYSTEM MENU")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_all_students()
        elif choice == "3":
            find_average_by_id()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Please enter a number between 1 and 4.")

        print()  # just a blank line to separate each round


main()
