import json
import pickle
from enum import Enum


class SerializeManager:

    def __init__(self, filename, fileType):
        self.filename = filename
        self.fileType = fileType.value

    def __enter__(self):
        if self.fileType == 1:
            self.file = open(self.filename, "w")
        if self.fileType == 2:
            self.file = open(self.filename, "wb")
        return self
    
    def __exit__(self, type, value, traceback):
        self.file.close()

    def serialize(self, obj):
        if self.fileType == 1:
            json.dump(obj, self.file)
        if self.fileType == 2:
            pickle.dump(obj, self.file)
    

class FileType(Enum):
    JSON = 1
    BYTE = 2

def serialize(object, filename, fileType):
    with SerializeManager(filename, fileType) as manager:
        manager.serialize(object)


user_dict = {'name': 'Roman', 'id': 8}
serialize(user_dict, "2.txt", FileType.BYTE)
serialize("String", "string.json", FileType.JSON)