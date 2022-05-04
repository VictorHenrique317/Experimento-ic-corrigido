import json
import os
class Configs():
    __configs = None
    def __init__(self) -> None:
        pass

    @staticmethod
    def readConfigFile(path):
         with open(path, "r") as file:
            Configs.__configs = json.load(file)

    @staticmethod
    def getParameter(parameter):
        return Configs.__configs[parameter]