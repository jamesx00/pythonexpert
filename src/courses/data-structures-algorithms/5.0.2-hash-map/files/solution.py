class HashMap:
    def __init__(self):
        self._buckets = [[] for _ in range(8)]
        self._size = 0

    def __len__(self):
        return self._size

    def bucket_count(self):
        return len(self._buckets)

    def _bucket_index(self, key):
        return hash(key) % len(self._buckets)

    def put(self, key, value):
        bucket = self._buckets[self._bucket_index(key)]
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return
        bucket.append([key, value])
        self._size += 1
        if self._size > 0.75 * len(self._buckets):
            self._resize(2 * len(self._buckets))

    def get(self, key):
        for k, v in self._buckets[self._bucket_index(key)]:
            if k == key:
                return v
        raise KeyError(key)

    def remove(self, key):
        bucket = self._buckets[self._bucket_index(key)]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self._size -= 1
                return
        raise KeyError(key)

    def _resize(self, new_count):
        old_buckets = self._buckets
        self._buckets = [[] for _ in range(new_count)]
        for bucket in old_buckets:
            for key, value in bucket:
                self._buckets[self._bucket_index(key)].append([key, value])
