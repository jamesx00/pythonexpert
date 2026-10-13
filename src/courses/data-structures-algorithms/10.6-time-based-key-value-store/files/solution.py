import bisect


class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key, value, timestamp):
        self.store.setdefault(key, []).append((timestamp, value))

    def get(self, key, timestamp):
        entries = self.store.get(key, [])
        i = bisect.bisect_right(entries, (timestamp, chr(0x10FFFF)))
        return entries[i - 1][1] if i > 0 else ""
