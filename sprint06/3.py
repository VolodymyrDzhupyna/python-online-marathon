import json
import jsonschema
from jsonschema import validate
import csv


class DepartmentName(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class InvalidInstanceError(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


def validate_json(json_data, validation_schema):
    try:
        validate(instance=json_data, schema=validation_schema)
    except jsonschema.exceptions.ValidationError:
        return False
    return True


student_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "name": {"type": "string"},
            "department_id": {"type": "number"},
        },
        "required": ["department_id", "name"]
    }
}

department_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "name": {"type": "string"}
        },
        "required": ["id", "name"]
    }
}


def user_with_department(user_department_csv, user_json, department_json):
    with open(user_json, "r") as f:
        user_list = json.load(f)
        if not validate_json(user_list, student_schema):
            raise InvalidInstanceError("Error in user schema")
    with open (department_json, "r") as f:
        department_list = json.load(f)
        if not validate_json(department_list, department_schema):
            raise InvalidInstanceError("Error in department schema")
    
    id_name_dict = dict((element["id"], element["name"]) for element in department_list)

    user_with_dep = []
    for element in user_list:
        try:
            user_with_dep.append({"name": element["name"], "department": id_name_dict[element["department_id"]]})
        except Exception:
            raise DepartmentName("Department with id {} doesn't exists".format(element["department_id"]))

    with open(user_department_csv, "wt") as f:
        csv.writer = csv.DictWriter(f, fieldnames=["name", "department"])
        csv.writer.writeheader()
        csv.writer.writerows(user_with_dep)


user_with_department("my.csv", "json_for_test/user.json", "json_for_test/department_without_id.json")