class CreateLog:
    def __init__(self, err_msg):
        self.err_msg = err_msg
        self.write_log()

    def write_log(self):
        try:
            f = open("log.txt", "a")
            f.write(self.err_msg)
            f.close()
        except Exception as ex:
            f = open("log.txt", "a")
            f.write(f"ReadyDriver -> GetDriver -> write_log -> {type(ex).__name__}")
            f.close()