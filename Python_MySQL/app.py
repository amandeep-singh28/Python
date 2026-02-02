from main import AdmissionDB

def menu():
    print("\n===== Admission Management System =====")
    print("1. Add Student")
    print("2. Apply for Admission")
    print("3. View Applications")
    print("4. Approve Application")
    print("5. Reject Application")
    print("6. Exit")

db = AdmissionDB()

while True:
    menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter name: ")
        email = input("Enter email: ")
        phone = input("Enter phone: ")
        city = input("Enter city: ")
        db.add_student(name, email, phone, city)

    elif choice == 2:
        application_id = int(input("Enter application id: "))
        student_id = int(input("Enter student id: "))
        course = input("Enter course: ")
        marks = int(input("Enter marks: "))
        applied_date = input("Enter applied date (YYYY-MM-DD): ")
        db.apply_for_admission(application_id, student_id, course, marks, applied_date)

    elif choice == 3:
        db.view_all_applications()

    elif choice == 4:
        print("Approve Application")
        db.update_status()

    elif choice == 5:
        print("Reject Application")
        db.update_status()

    elif choice == 6:
        db.close()
        print("Exiting program...")
        break

    else:
        print("Invalid choice, try again.")
