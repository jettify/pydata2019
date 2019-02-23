with self.condition:
    while self.is_empty():
        self.condition.wait()
    item = self.buffer[self.head]
    self.buffer[self.head] = None
    self.head = self._next(self.head)
    self.size -= 1

    # notify_all() avoids deadlocks because both consumers
    # and producers are notified
    self.condition.notify_all()
    return item

# CPython implementation
    # https://github.com/python/cpython/blob/df5cdc11123a35065bbf1636251447d0bfe789a5/Lib/queue.py#L43-L49
    # Notify not_empty whenever an item is added to the queue;
    self.not_empty = threading.Condition(self.mutex)
    # Notify not_full whenever an item is removed from the queue;
    self.not_full = threading.Condition(self.mutex)
