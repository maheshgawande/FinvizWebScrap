import datetime

class CreateLog:
    call_count = 0

    def __init__(self, err_msg):
        CreateLog.call_count += 1
        self.err_msg = err_msg
        self.log_time = datetime.datetime.now()
        self.write_log()

    def write_log(self):
        date = self.log_time.strftime("%d")
        month = self.log_time.strftime("%m")
        hour = self.log_time.strftime("%H")
        minute = self.log_time.strftime("%M")
        seconds = self.log_time.strftime("%S")
        file_name = f"Logs/log_{date}-{month}.txt"
        
        try:
            f = open(file_name, "a")
            f.write(f"({hour}:{minute}:{seconds}00){self.err_msg}\n")
            f.close()
        except Exception as ex:
            f = open(f"log_{date}-{month}.txt", "a")
            f.write(f"({hour}:{minute}:{seconds}00)ReadyDriver -> GetDriver -> write_log -> {type(ex).__name__}\n")
            f.close()