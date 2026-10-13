class HashMap:
    def __init__(self):
        # Each bucket is a list of [key, value] pairs.
        self._buckets = [[] for _ in range(8)]
        self._size = 0

    def __len__(self):
        return self._size

    def bucket_count(self):
        return len(self._buckets)

    def _bucket_index(self, key):
        return hash(key) % len(self._buckets)

    def put(self, key, value):
        pass

    def get(self, key):
        raise KeyError(key)

    def remove(self, key):
        pass
