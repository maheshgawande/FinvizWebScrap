# from selenium import webdriver
import ReadyDriver

class WebScrap(ReadyDriver):
    def __init__(self, url):
        self.url = url

    def open_url(self):
        self.driver.get(self.url)
        # try:
        #     self.driver.get(self.url)
        # except Exception as ex:
        #     print(f'Error in WebScrap.open_url: {type(ex).__name__}')
        #     driver.quit()
    
    def find_element(self, element):
        pass

    def driver_close(self):
        driver.quit()

if __name__ == '__main__':
    url = "http://www.google.com"

    wb = WebScrap(url)
    
    wb.open_url()