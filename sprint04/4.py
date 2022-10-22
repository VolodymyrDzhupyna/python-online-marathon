class Testpaper:

    def __init__(self, subject, markscheme, pass_mark):
        self.subject = subject
        self.markscheme = markscheme
        self.pass_mark = pass_mark


class Student:
    
    def __init__(self):
        self.__tests_taken = {}
    
    @property
    def tests_taken(self):
        if not self.__tests_taken:
            return "No tests taken"
        return self.__tests_taken

    def take_test(self, testpaper, students_answers):
        count_pass_mark = 0

        for item in students_answers:
            if item in testpaper.markscheme:
                count_pass_mark += 1
        actual_mark = round(count_pass_mark * 100 / len(testpaper.markscheme))
        int_pass_mark = int(testpaper.pass_mark.replace(testpaper.pass_mark[-1], ""))

        if actual_mark >= int_pass_mark:
            self.__tests_taken[testpaper.subject] = f"Passed! ({actual_mark}%)"
        else:
            self.__tests_taken[testpaper.subject] = f"Failed! ({actual_mark}%)"


paper1 = Testpaper("Maths", ["1A", "2C", "3D", "4A", "5A"], "60%")
paper2 = Testpaper("Chemistry", ["1C", "2C", "3D", "4A"], "75%")
paper3 = Testpaper("Computing", ["1D", "2C", "3C", "4B", "5D", "6C", "7A"], "75%")

student1 = Student()
student1.take_test(paper1, ["1A", "2D", "3D", "4A", "5A"])
print(student1.tests_taken)

student2 = Student()
student2.take_test(paper2, ["1C", "2D", "3A", "4C"])
student2.take_test(paper3, ["1A", "2C", "3A", "4C", "5D", "6C", "7B"])
print(student2.tests_taken)
