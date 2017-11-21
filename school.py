import json


def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError

class School:
    'day la School class'

    #Phuong thuc khoi tao doi tuong
    def __init__(self, id, name, username, password, filepath= None, predict = None ):
        self.id = id
        self.name = name
        self.username = username
        self.password = password
        self.filepath = filepath
        self.predict = predict

    # def __init__(self, name, username, password):
    #     self.name  = name
    #     self.username = username
    #     self.password = password

    def getName(self):
        return self.name

    def getUsername(self):
        return self.usename

    def getPassword(self):
        return self.password

    def getFilepath(self):
        return self.filepath

    def getPredict(self):
        return self.predict

    def serialize(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "username" : self.username,
            "password" : self.password,
            "filepath" : self.filepath,
            "predict" : self.predict
        }


