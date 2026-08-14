# dict that holds the keys, 
# values can be tuples (timestamp, value)
# stored in a list

# use key to look up the list
# iterate from end and find timestamp in list less than timestamp input
# return value 

class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time_map:
            self.time_map[key].append((timestamp, value))
        else:
            self.time_map[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        for inner_timestamp, value in reversed(self.time_map[key]):
            if inner_timestamp <= timestamp:
                return value
        return ""
