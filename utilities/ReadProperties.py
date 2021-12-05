import configparser
import os

conf = configparser.RawConfigParser()
conf.read(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\configfiles\\config.ini")

"""
# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# C:\\Users\\shara\\PycharmProjects\\SwagLabs-PythonHybridFramework\\configfiles\\config.ini
"""


class ConfigData:
    @staticmethod
    def getusertype():
        usertype = conf.get('common-info', 'usertype'.strip())
        return usertype


print(ConfigData.getusertype())
