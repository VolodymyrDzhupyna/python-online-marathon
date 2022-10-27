import unittest
from unittest.mock import patch, mock_open


def file_parser(file_name, find_str, *replace_str):
    if not replace_str:
        with open(file_name, "r") as f:
            data = f.read()
        return f"Found {data.count(find_str)} strings"
    if file_name and find_str and replace_str:
        replace_counter = 0
        with open(file_name, "r+") as f:
            data = f.read()
            for item in data:
                if item == find_str:
                    data = data.replace(find_str, replace_str[0])
                    replace_counter += 1
            f.write(data)
        return  f"Replaced {replace_counter} strings"


class ParserTest(unittest.TestCase):
    
    def test_first_file_parser(self):
        file_content_mock = "Soft Serve Academy. Hello, Academy"

        with patch("builtins.open", new=mock_open(read_data=file_content_mock)) as file_mock:
            file_parser(file_mock, "a", "x")
            file_mock.assert_called_once()
            handle = file_mock()
            handle.write.assert_called_once_with(file_content_mock.replace("a", "x"))

    def test_second_file_parser(self):
        file_content_mock = "Soft Serve Academy. Hello, Academy. How are you?"

        with patch("builtins.open", new=mock_open(read_data=file_content_mock)) as file_mock:
            file_parser(file_mock, "e", "l")
            file_mock.assert_called_once()
            handle = file_mock()
            handle.write.assert_called_once_with(file_content_mock.replace("e", "l"))


print(file_parser("my_file.txt", "s", "m"))
print(file_parser("my_file.txt", "s"))
