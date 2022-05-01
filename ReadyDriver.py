from selenium import webdriver
from os.path import exists

class GetDriver:
    def __init__(self):
        self.path = "C:\Program Files (x86)\chromedriver.exe"
        self.driver = webdriver.Chrome(path)

    def open_driver(self):
        if(self.check_path()):
            self.driver.get(self.path)
            return self.driver
        else:
            err_msg = "ReadyDriver -> GetDriver -> open_driver -> Failed to open driver!"
            self.write_log(err_msg)
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
            return False

    def write_log(self, err_msg):
        try:
            f = open("log.txt", "a")
            f.write(err_msg)
            f.close()
        except Exception as ex:
            f = open("log.txt", "a")
            f.write(f"ReadyDriver -> GetDriver -> write_log -> {type(ex).__name__}")
            f.close()