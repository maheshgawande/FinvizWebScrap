from selenium import webdriver
from os.path import exists
from Log import CreateLog

class GetDriver:
    def __init__(self):
        self.path = "C:\Program Files (x86)\chromedriver.exe"

    def open_driver(self):
        if(self.check_path()):
            driver = webdriver.Chrome(self.path)
            return driver
        else:
            err_msg = "ReadyDriver -> GetDriver -> open_driver -> Failed to open driver!"
            Createog(err_msg)
            return False

    def close_driver(self):
        get_status(self.driver)
        if():
            pass
        else:
            pass

    def check_path(self):
        if(exists(self.path)):
            return True
        else:
            err_msg = "ReadyDriver -> GetDriver -> check_path -> Driver file does bot exists!"
            CreateLog(err_msg)
            return False