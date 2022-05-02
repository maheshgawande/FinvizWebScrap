from selenium import webdriver
from os.path import exists
from Log import CreateLog

class GetDriver:
    def __init__(self):
        self.path = "C:\Program Files (x86)\chromedriver.exe"

    def open_driver(self):
        driver = False
        err_msg = ""
        path_exists = self.check_path()

        if(path_exists):
            d = webdriver.Chrome(self.path)
            err_msg = "ReadyDriver.py-->GetDriver-->open_driver--> Driver initialized successfully!"
            driver = d
        else:
            err_msg = "ReadyDriver.py-->GetDriver-->open_driver--> Failed to open driver!"
            driver = False
        
        CreateLog(err_msg)
        return driver

    def close_driver(self):
        try:
            self.driver.quit()
            err_msg = "ReadyDriver.py-->GetDriver-->close_driver--> Driver closed successfully!"
        except Exception as ex:
            err_msg = f"ReadyDriver.py-->GetDriver-->close_driver--> {type(ex).__name__}"
            pass

        CreateLog(err_msg)

    def check_path(self):
        ret = False
        if(exists(self.path)):
            err_msg = "ReadyDriver.py-->GetDriver-->check_path--> Driver file exists!"
            ret = True
        else:
            err_msg = "ReadyDriver.py-->GetDriver-->check_path--> Driver file does not exists!"
            ret = False

        CreateLog(err_msg)
        return ret