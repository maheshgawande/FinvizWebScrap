from _driver import GetDriver
from Log import CreateLog
from selenium.webdriver.support.ui import Select

class WebScrap:
    call_count = 0

    def __init__(self, url):
        WebScrap.call_count += 1
        self.gt = None

        if WebScrap.call_count == 1:
            self.session_start()
            self.gt = GetDriver()

        self.url = url
        self.driver = self.gt.open_driver()
    
    def session_start(self):
        log_msg = "-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/---- Session Start ----/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/"
        CreateLog(log_msg)

    def open_url(self):
        open_true = False
        if(self.driver != False):
            self.driver.get(self.url)
            log_msg = "Main.py-->WebScrap-->open_url--> URL invoked successfully!"
            open_true = True
        else:
            log_msg = "Main.py-->WebScrap-->open_url--> Failed to open URL!"

        CreateLog(log_msg)
        return open_true

    def select_ddl(self, ddl_name, ddl_value):
        try:
            ddl_dict = {
                "sector": "fs_sec",
                "industry": "fs_ind",
                "country": "fs_geo", 
                "average volume": "fs_sh_avgvol",
                "price": "fs_sh_price", 
                "52-week hi/lo": "fs_ta_highlow52w"
            }
            
            if len(ddl_name) > 0:
                ddl = self.driver.find_element_by_id(ddl_dict[ddl_name])
                select = Select(ddl)
                select.select_by_visible_text(ddl_value)
                log_msg = f"Main.py-->WebScrap-->select_ddl--> \"{ddl_value}\" value selected for \"{ddl_name}\"."

        except Exception as ex:
            log_msg = f"Main.py-->WebScrap-->select_ddl--> {type(ex).__name__}"

        CreateLog(log_msg)
    
    def session_end(self):
        self.gt.close_driver()
        log_msg = "-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/---- Session End ----/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/\n"
        CreateLog(log_msg)
    
    def __del__(self):
        self.session_end()

if __name__ == '__main__':
    url = "https://finviz.com/screener.ashx?v=111&ft=4"
    url_len = len(url)
    http_contains = url.__contains__("https://")

    if url_len >= 14 & http_contains:
        try:
            wb = WebScrap(url)
            
            url_open = wb.open_url()
            
            if url_open:
                ddl_list = ["sector", "industry", "country", "average volume", "price", "52-week hi/lo"]
                ddl_value = ["Technology", "Semiconductors", "USA", "", "", ""]

                for i in range(len(ddl_list)): 
                    wb.select_ddl(ddl_list[i], ddl_value[i])
        except Exception as ex:
            log_msg = f"Main.py-->__main__--> {type(ex).__name__}"
            CreateLog(log_msg)
        finally:
            # log_msg = "-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/---- Session End ----/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-\n"
            # CreateLog(log_msg)
            del wb