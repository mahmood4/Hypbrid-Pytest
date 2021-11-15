import configparser
#pytest -v -s -n=2 --capture sys -rP --html=Reports\repts.html .\testCases\test_login.py --browser chrome

config=configparser.RawConfigParser()
#config.read('..\\Configurations\\config.ini')
config.read('C:\\Users\\user\\PycharmProjects\\Hybrid-Pytest\\Configurations\\config.ini')

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info','baseURL')
        return url

    @staticmethod
    def getUseremail():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password