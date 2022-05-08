from selenium import webdriver
from os.path import exists
from Log import CreateLog

class GetDriver:
    def __init__(self):
        self.path = "C:\Program Files (x86)\chromedriver.exe"
        self.driver = None

    def open_driver(self):
        self.driver = False
        log_msg = ""
        path_exists = self.check_path()

        if(path_exists):
            d = webdriver.Chrome(self.path)
            log_msg = "ReadyDriver.py-->GetDriver-->open_driver--> Driver initialized successfully!"
            self.driver = d
        else:
            log_msg = "ReadyDriver.py-->GetDriver-->open_driver--> Failed to open self.driver!"
            self.driver = False
        
        CreateLog(log_msg)
        return self.driver

    def close_driver(self):
        try:
            self.driver.quit()
            log_msg = "ReadyDriver.py-->GetDriver-->close_driver--> Driver closed successfully!"
        except Exception as ex:
            log_msg = f"ReadyDriver.py-->GetDriver-->close_driver--> {type(ex).__name__}"
            pass

        CreateLog(log_msg)

    def check_path(self):
        ret = False
        if(exists(self.path)):
            log_msg = "ReadyDriver.py-->GetDriver-->check_path--> Driver file exists!"
            ret = True
        else:
            log_msg = "ReadyDriver.py-->GetDriver-->check_path--> Driver file does not exists!"
            ret = False

        CreateLog(log_msg)
        return ret