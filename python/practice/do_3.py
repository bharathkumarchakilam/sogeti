class stuTable:
    def __init__(self, id, name, standard):
        self.id = id
        self.name = name
        self.standard = standard


class MarkTable:
    def __init__(self, id, mark):
        self.id = id
        self.mark = mark


class SqlOperation:
    def __init__(self, students, marks):
        self.students = students
        self.marks = marks

    def joinTable(self):
        student_marks = {mark.id for mark in self.marks}
        return [student for student in self.students
                if student.id in student_marks]

    def selectByStandard(self, standard):
        return [student.name for student in self.students
                if student.standard == standard]
