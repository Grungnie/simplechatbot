from configparser import ConfigParser
import os

def ConfigSectionMap(section):
    if isinstance(section, str):
        section_list = [section]
    else:
        section_list = section
    config = ConfigParser()
    config.read('{}/config.ini'.format(os.getcwd()))
    return {key: value for section in section_list for key, value in config[section].items()}
