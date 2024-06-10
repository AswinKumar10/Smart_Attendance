def mark_attendance(student_id):
    with open('attendance.txt', 'a') as file:
        file.write(f'{student_id}\n')

def view_attendance():
    with open('attendance.txt', 'r') as file:
        attendance_list = file.readlines()
    return attendance_list

def main():
    while True:
        print("Welcome to the Student Attendance System")
        print("1. Mark Attendance")
        print("2. View Attendance")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            student_id = input("Enter student ID: ")
            mark_attendance(student_id)

        elif choice == '2':
            attendance_list = view_attendance()
            print("\nAttendance List")
            for record in attendance_list:
                print(record.strip())

        elif choice == '3':
            break
        
        else:
            print("Invalid choice")

if __name__ == '__main__':
    main()

