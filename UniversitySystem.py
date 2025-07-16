class Student:
    def __init__(self, id, name, email):
        self.__id = id
        self.__name = name
        self.__email = email

    def getStudentID(self):
        return self.__id

    def getStudentName(self):
        return self.__name

    def getStudentEmail(self):
        return self.__email

    def updateStudentName(self, newname):
        self.__name = newname

    def updateStudentID(self, newid):
        self.__id = newid

    def updateStudentEmail(self, newemail):
        self.__email = newemail

    def display_student_info(self):
        print(f"Student name = {self.getStudentName()} and his id:{self.getStudentID()} and his email[{self.getStudentEmail()}]")

class Classroom:
    def __init__(self, name):
        self.__name = name
        self.__students = []

    def getClassroomName(self):
        return self.__name

    def getStudents(self):
        return self.__students

    def updateClassroomName(self, newname):
        self.__name = newname

    def addStudent(self, student):
        self.__students.append(student)

    def removeStudentFromClassroom(self, id):
        for student in self.__students:
            if id == student.getStudentID():
                self.__students.remove(student)
                print("Student removed successfully")
                break
        else:
            print("Student not found")

    def displayStudentsInClassroom(self):
        counter = 1
        for student in self.__students:
            print(f"Student{counter} name is:{student.getStudentName()} and his id:{student.getStudentID()} and his email={student.getStudentEmail()}")
            counter += 1

class Professor:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__subjects = []

    def getProfessorID(self):
        return self.__id

    def getProfessorName(self):
        return self.__name

    def getSubjects(self):
        return self.__subjects

    def updateProfessorName(self, newname):
        self.__name = newname

    def updateProfessorID(self, newid):
        self.__id = newid

    def addSubject(self, subject):
        self.__subjects.append(subject)

    def displayProfessorInfo(self):
        print(f"Professor name = {self.getProfessorName()} and his id:{self.getProfessorID()} and his subjects[{self.getSubjects()}]")

class Grade:
    def __init__(self, student, subject, grade):
        self.__student = student
        self.__subject = subject
        self.__grade = grade

    def getStudent(self):
        return self.__student

    def getSubject(self):
        return self.__subject

    def getGrade(self):
        return self.__grade

    def updateGrade(self, newgrade):
        self.__grade = newgrade

    def displayGradeInfo(self):
        print(f"Student name = {self.__student.getStudentName()} and his id:{self.__student.getStudentID()} and his grade in {self.__subject} is {self.__grade}")

class Attendance:
    def __init__(self, student, date, status):
        self.__student = student
        self.__date = date
        self.__status = status

    def getStudent(self):
        return self.__student

    def getDate(self):
        return self.__date

    def getStatus(self):
        return self.__status

    def updateStatus(self, newstatus):
        self.__status = newstatus

    def displayAttendanceInfo(self):
        print(f"{self.getStudent().getStudentName()} status is {self.__status}")

class University:
    def __init__(self):
        self.students = []
        self.classrooms = []
        self.professors = []
        self.grades = []
        self.attendance_records = []

    def addStudent(self, student):
        self.students.append(student)
        print("Student added successfully")

    def removeStudent(self, id):
        for student in self.students:
            if id == student.getStudentID():
                self.students.remove(student)
                print("Student removed successfully")
                break
        else:
            print("Student not found")

    def displayStudents(self):
        counter = 1
        for student in self.students:
            print(f"Student{counter} name is:{student.getStudentName()} and his id:{student.getStudentID()} and his email={student.getStudentEmail()}")
            counter += 1

    def addClassroom(self, classroom):
        self.classrooms.append(classroom)
        print("Classroom added successfully")

    def removeClassroom(self, name):
        for classroom in self.classrooms:
            if name == classroom.getClassroomName():
                self.classrooms.remove(classroom)
                print("Classroom removed successfully")
                break
        else:
            print("Classroom not found")

    def displayClassrooms(self):
        counter = 1
        for classroom in self.classrooms:
            print(f"Classroom{counter} name is:{classroom.getClassroomName()}")
            counter += 1

    def addProfessor(self, professor):
        self.professors.append(professor)
        print("Professor added successfully")

    def removeProfessor(self, id):
        for professor in self.professors:
            if id == professor.getProfessorID():
                self.professors.remove(professor)
                print("Professor removed successfully")
                break
        else:
            print("Professor not found")

    def displayProfessors(self):
        counter = 1
        for professor in self.professors:
            print(f"Professor{counter} name is:{professor.getProfessorName()} and his id:{professor.getProfessorID()}")
            counter += 1

    def addGrade(self, grade):
        self.grades.append(grade)

    def updateGrade(self, student_id, newgrade):
        for grade in self.grades:
            if student_id == int(grade.getStudent().getStudentID()):
                grade.updateGrade(newgrade)
                print("Grade updated successfully")
                break
        else:
            print("Not found")

    def displayGrades(self):
        counter = 1
        for grade in self.grades:
            print(f"Student{counter} whose id is {grade.getStudent().getStudentID()} his grade = {grade.getGrade()}")
            counter += 1

    def addAttendance(self, attendance_info):
        self.attendance_records.append(attendance_info)

    def updateAttendanceStatus(self, student_id, newstatus):
        for record in self.attendance_records:
            if student_id == record.getStudent().getStudentID():
                record.updateStatus(newstatus)
                print("Attendance status updated successfully")
                break
        else:
            print("Not found")

    def displayAttendance(self):
        counter = 1
        for record in self.attendance_records:
            print(f"Student{counter} whose id is {record.getStudent().getStudentID()} his status = {record.getStatus()} at {record.getDate()}")
            counter += 1

class System:
    def __init__(self):
        self.system = University()

    def main(self):
        while True:
            choice = int(input("\nChoose one:\n1-Add Student\n2-Remove Student\n3-Display Students\n4-Add Classroom\n5-Remove Classroom\n6-Display Classrooms\n7-Add Professor\n8-Remove Professor\n9-Display Professors\n10-Add Grade\n11-Update Grade\n12-Display Grades\n13-Add Attendance\n14-Update Attendance Status\n15-Display Attendance\n16-Exit\n"))

            if choice == 1:
                student_id = int(input("Enter student id:"))
                student_name = input("Enter student name:")
                student_email = input("Enter student email:")
                student = Student(student_id, student_name, student_email)
                self.system.addStudent(student)

            elif choice == 2:
                student_id = int(input("Enter student id to remove:"))
                self.system.removeStudent(student_id)

            elif choice == 3:
                self.system.displayStudents()

            elif choice == 4:
                classroom_name = input("Enter classroom name:")
                classroom = Classroom(classroom_name)
                self.system.addClassroom(classroom)

            elif choice == 5:
                classroom_name = input("Enter classroom name to remove:")
                self.system.removeClassroom(classroom_name)

            elif choice == 6:
                self.system.displayClassrooms()

            elif choice == 7:
                professor_id = int(input("Enter professor id:"))
                professor_name = input("Enter professor name:")
                professor = Professor(professor_id, professor_name)
                self.system.addProfessor(professor)

            elif choice == 8:
                professor_id = int(input("Enter professor id to remove:"))
                self.system.removeProfessor(professor_id)

            elif choice == 9:
                self.system.displayProfessors()

            elif choice == 10:
                student_id = int(input("Enter student id:"))
                for student in self.system.students:
                    if student_id == int(student.getStudentID()):
                        subject = input("Enter subject:")
                        grade = int(input("Enter grade:"))
                        grade_obj = Grade(student, subject, grade)
                        self.system.addGrade(grade_obj)
                        print("Grade added successfully")
                        break
                else:
                    print("Not found")

            elif choice == 11:
                student_id = int(input("Enter student id:"))
                newgrade = int(input("Enter new grade:"))
                self.system.updateGrade(student_id, newgrade)

            elif choice == 12:
                self.system.displayGrades()

            elif choice == 13:
                student_id = int(input("Enter student id:"))
                for student in self.system.students:
                    if student_id == student.getStudentID():
                        date = input("Enter the date:")
                        status = input("Enter the status:")
                        attendance = Attendance(student, date, status)
                        self.system.addAttendance(attendance)
                        print("Attendance added successfully")
                        break
                else:
                    print("Not found")

            elif choice == 14:
                student_id = int(input("Enter student id:"))
                newstatus = input("Enter new status:")
                self.system.updateAttendanceStatus(student_id, newstatus)

            elif choice == 15:
                self.system.displayAttendance()

            elif choice == 16:
                break

            else:
                print("Invalid choice")
start = System()
start.main()