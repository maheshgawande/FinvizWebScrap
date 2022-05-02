from selenium import webdriver
from os.path import exists
from Log import CreateLog

class GetDriver:
    def __init__(self):
        self.path = "C:\Program Files (x86)\chromedriver.exe"

    def open_driver(self):
        driver = False
        err_msg = ""
        if(self.check_path()):
            d = webdriver.Chrome(self.path)
            err_msg = "ReadyDriver -> GetDriver -> open_driver -> Driver initialized!"
            driver = d
        else:
            err_msg = "ReadyDriver -> GetDriver -> open_driver -> Failed to open driver!"
            driver = False
        
        CreateLog(err_msg)
        return driver

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