import json
import logging
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


def parse_user(output_file, *input_files):
    result = {}
    my_list = []
    
    for files in input_files:
        try:
            with open(files, 'r') as in_file:
                data = json.load(in_file)
                my_list.append(data)
        except OSError:
                logging.error(f"File {files} doesn't exist")

    try:
        for data in my_list:
            for item in data:
                name = item['name']
                if name not in result:
                    result[name] = item
    except KeyError:
        with open(output_file, 'w') as out_file:
            json.dump("[]", out_file)

    with open(output_file, 'w') as out_file:
        json.dump(list(result.values()), out_file, indent=4)
    

parse_user("user3.json", "json_for_test/user1.json", "json_for_test/user2.json")
parse_user("user4.json", "json_for_test/user3a.json", "json_for_test/user3b.json")
