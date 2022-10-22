import json


def find(file, key):
    value_list = []
    unique_value_list = []

    with open (f"{file}", "r") as read_file:
        data = read_file.read()

    def check_dict(my_dict):
        if key in my_dict.keys() and my_dict[key] not in value_list:
            if isinstance(my_dict[key], list):
                value_list.extend(my_dict[key])
            else:
                value_list.append(my_dict[key])

    try:
        json.loads(data, object_hook=check_dict)
    except KeyError:
        return value_list
    for item in value_list:
        if item not in unique_value_list:
            unique_value_list.append(item)
    return unique_value_list


print(find("json_for_test/new.json", "password"))
print(find("json_for_test/example.json", "password"))
print(find("json_for_test/without_pass.json", "password"))
