class School:
    dict = {'1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': [], '10': [] }
    def __init__(self, grade_school = dict ):
        self.grade_school = grade_school

    def add_student(self, name, grade):
        self.grade_school.setdefault(grade, []).append(name)
        return 'OK'

    def roster(self):
        dict_list = []
        total_students = []
        dict_list =  list(self.grade_school.values())
        for value in dict_list:
                    total_students.extend(value)
        return total_students

    def grade(self, grade_number):
        return (self.grade_school[grade_number])
