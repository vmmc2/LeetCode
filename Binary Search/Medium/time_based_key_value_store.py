class TimeMap:
    def __init__(self):
        self.cache = {} # This maps each key to a list where each element is composed of a timestamp and a value

    def binarySearch(self, l: List[tuple], timestamp: int) -> int:
        n = len(l)
        left, right = 0, n - 1
        idx = -1

        while left <= right:
            mid = (left + right) // 2
            if timestamp == l[mid][0]:
                idx = mid
                break
            elif timestamp > l[mid][0]:
                idx = mid
                left = mid + 1
            else:
                right = mid - 1

        return idx

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.cache:
            self.cache[key] = []
        self.cache[key].append((timestamp, value))
        return

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.cache:
            return ""
        
        resultIdx = self.binarySearch(self.cache[key], timestamp)
        if resultIdx == -1:
            return ""
        else:
            return self.cache[key][resultIdx][1]
        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)