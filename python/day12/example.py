class StuTable:
    def __init__(self, id: int, name: str, standard: int):
        self.id = id
        self.name = name
        self.standard = standard


class MarkTable:
    def __init__(self, id: int, mark: int):
        self.id = id
        self.mark = mark


class SqlOperation:
    def __init__(self, students: list, marks: list):
        self.students = students
        self.marks = marks

    def joinTable(self):
        """Returns a list of students with their marks."""
        joined_data = []
        for student in self.students:
            for mark in self.marks:
                if student.id == mark.id:
                    joined_data.append((student.id, student.name, student.standard, mark.mark))
        return joined_data

    def selectByStandard(self, standard: int):
        """Returns a list of student names in the given standard."""
        return [student.name for student in self.students if student.standard == standard]


# Example usage
students = [
    StuTable(1, "Alice", 10),
    StuTable(2, "Bob", 10),
    StuTable(3, "Charlie", 11),
]

marks = [
    MarkTable(1, 85),
    MarkTable(2, 90),
    MarkTable(3, 88),
]

sql_op = SqlOperation(students, marks)

# Joining student and marks tables
print(sql_op.joinTable())

# Selecting students by standard
print(sql_op.selectByStandard(10))
