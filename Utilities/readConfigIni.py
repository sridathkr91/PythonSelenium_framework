import configparser
obj1=configparser.RawConfigParser()
obj1.read(".\\Configurations\\config.ini")

class Utility_readConfigIni:

    @staticmethod
    def readURL():
        url=obj1.get('common data','URL')
        return url

    @staticmethod
    def readFullName():
        fullName=obj1.get('testData for testTextBox1','FULLNAME')
        return fullName

    @staticmethod
    def readEmail():
        email=obj1.get('testData for testTextBox1','EMAIL')
        return email

    @staticmethod
    def readCurrAddress():
        CurrAddress=obj1.get('testData for testTextBox1','CURRENT_ADDRESS')
        return CurrAddress

    @staticmethod
    def readPermAddress():
        permanentAddress= obj1.get('testData for testTextBox1', 'PERMANENT_ADDRESS')
        return permanentAddress

    @staticmethod
    def returnExcelPath():
        path=obj1.get('common data','PATH_TO_EXCELTC01')
        return path