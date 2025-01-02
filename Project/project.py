class School:
    pass

class Student(School):
    def __init__(
        self,
        student_id,
        student_name,
        student_f_name,
        student_phone_number,
        student_address,
        student_fees
        ):
        self.student_id = student_id
        self.student_name = student_name
        self.student_f_name = student_f_name
        self.student_phone_number = student_phone_number
        self.student_address = student_address
        self.student_fees = student_fees   

    def getStudent(self):    
        return f"id = {self.student_id},name = {self.student_name},father name = {self.student_f_name},phone number = {self.student_phone_number},address = {self.student_address},fee = {self.student_fees}"     

class Teacher(School):
    def __init__(
        self,
        teacher_id,
        teacher_name,
        teacher_f_name,
        teacher_phone_number,
        teacher_email,
        teacher_salary,
        teacher_subject,
        teacher_experience,
        teacher_address
    ):
        self.teacher_id = teacher_id
        self.teacher_name = teacher_name
        self.teacher_f_name = teacher_f_name
        self.teacher_phone_number = teacher_phone_number
        self.teacher_email = teacher_email
        self.teacher_salary = teacher_salary
        self.teacher_subject = teacher_subject
        self.teacher_experience = teacher_experience
        self.teacher_address = teacher_address

    def getTeacher(self):
        print("id = " + str(self.teacher_id) + ", name = " + self.teacher_name + ", father name = " + self.teacher_f_name + ", phone = " + self.teacher_phone_number + ", email = " + self.teacher_email + ", subject = " + self.teacher_subject + ", experience = " + str(self.teacher_experience) + " years, salary = " + str(self.teacher_salary) + ", address = " + self.teacher_address)

    def updateSalary(self, new_salary):
        self.teacher_salary = new_salary
        print("Salary updated to " + str(self.teacher_salary))

    def promoteTeacher(self):
        self.teacher_experience = self.teacher_experience + 1
        print(self.teacher_name + " promoted! Experience is now " + str(self.teacher_experience) + " years.")

    def assignSubject(self, subject):
        self.teacher_subject = subject
        print("Assigned subject: " + self.teacher_subject)

    def updateContact(self, phone, email, address):
        self.teacher_phone_number = phone
        self.teacher_email = email
        self.teacher_address = address
        print("Contact details updated: Phone - " + self.teacher_phone_number + ", Email - " + self.teacher_email + ", Address - " + self.teacher_address)

class Admin(School):
    pass

class Classrooms(School):
    pass
    
class Event(School):
    pass

class Exams(School):
    pass
  
class Stock(School):
    pass
