class Student:

    def __init__(self, model, controller):
        self.__model = model
        self.__controller = controller

        self.students = []

        self.read_file()

    def read_file(self):
        file = open("src/store/student.csv", mode="r")

        for line in file:
            self.students.append(self.clear_line(line=line))

        file.close()

    def clear_line(self, line):
        return line.replace('\n', '').title()
