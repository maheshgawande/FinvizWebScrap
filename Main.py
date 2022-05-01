from ReadyDriver import GetDriver
from Log import CreateLog

class WebScrap:
    def __init__(self, url):
        self.url = url
        self.gt = GetDriver()
        self.driver = self.gt.open_driver()

    def open_url(self):
        if(self.driver != False):
            self.driver.get(self.url)
        else:
            err_msg = "Main.py -> WebScrap -> open_url(): Failed to open URL"
            CreateLog(err_msg)

    def find_element(self, element):
        pass

    def driver_close(self):
        driver.quit()

if __name__ == '__main__':
    url = "https://www.google.com/"

    wb = WebScrap(url)
    
    wb.open_url()