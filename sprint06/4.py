import json
from json import JSONEncoder


class Encoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

class Student:
    
    def __init__(self, full_name, avg_rank, courses):
        self.full_name = full_name
        self.avg_rank = avg_rank
        self.courses = courses
    
    @classmethod
    def from_json(cls, json_file):
        with open(json_file) as f:
            dictionary = json.load(f)
        return cls(**dictionary)

    def __str__(self):
        return f"{self.full_name} ({self.avg_rank}): {self.courses}"

    def serialize_to_json(self, filename):
        with open(filename, "w") as f:
            json.dump(self, f, cls=Encoder)
    
    @classmethod
    def serialize_list_to_json(cls, students, file):
        with open(file, "w") as f:
            json.dump(students, f, cls=Encoder)


class Group:

    def __init__(self, title):
        self.title = title
        self.students = []

    def __str__(self):
        return f"{self.title}: {[str(Student(**item)) for item in self.students]}"

    @classmethod
    def create_group_from_file(cls, students_file):
        with open(students_file) as f:
            students = json.load(f)
            g = Group(title=str(students_file).split(".")[0])
            if isinstance(students, list):
                g.students = students
            else:
                g.students = [students]
            return g
    
    @classmethod
    def serialize_to_json(cls, groups, file):
        with open(file, "w") as f:
            json.dump(groups, f, cls=Encoder)


g1 = Group.create_group_from_file("json_for_test/2020_2.json")
g2 = Group.create_group_from_file("json_for_test/2020-01.json")
Group.serialize_to_json([g1, g2], "g1")
