from typing import List
from collections import defaultdict
import bisect

# See details here https://wenshengchen.com/2020/02/24/981-time-based-key-value-store.html
class TimeMap:

    def __init__(self):
        self.hashmap = {}
        self.timestamps = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if (key, timestamp) not in self.hashmap:
            bisect.insort(self.timestamps[key], timestamp)

        self.hashmap[(key, timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:
        if (key, timestamp) in self.hashmap:
            return self.hashmap[(key, timestamp)]
        else:
            index = bisect.bisect(self.timestamps[key], timestamp)
            return "" if index == 0 else self.hashmap[(key, self.timestamps[key][index-1])]

## TEST CASES
obj = TimeMap()
obj.set("foo", "bar", 1)
assert obj.get("foo", 1) == "bar"
assert obj.get("foo", 3) == "bar"
obj.set("foo", "bar2", 4)
assert obj.get("foo", 4) == "bar2"
assert obj.get("foo", 5) == "bar2"

obj = TimeMap()
obj.set("love", "high", 10)
obj.set("love", "low", 20)
assert obj.get("love", 5) == ""
assert obj.get("love", 10) == "high"
assert obj.get("love", 15) == "high"
assert obj.get("love", 20) == "low"
assert obj.get("love", 25) == "low"

print('All Passed!')
