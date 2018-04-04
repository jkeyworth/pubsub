from configparser import ConfigParser
import os

class ConfigManager:


    def __init__(self, file_name):
        self.__config_parser = ConfigParser()
        self.__config_parser.read(
            [os.path.join(os.curdir, file_name),
             os.path.join(os.path.expanduser("~"), file_name),
             os.path.join(os.environ.get("MASCHINE_CONF"), file_name)])

if __name__ == "__main__":
    cm = ConfigManager("../tests/files/test_config.ini")
