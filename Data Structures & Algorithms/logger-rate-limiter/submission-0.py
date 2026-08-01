class Logger:

    def __init__(self):
        self.time_map = {} # {message : timestamp + 10}


    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.time_map and timestamp < self.time_map[message]:
            return False
        else:
            self.time_map[message] = timestamp + 10
            return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
