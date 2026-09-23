import threading


class ThreadSafeCounter:
    def __init__(self):
        self.lock = threading.Lock()
        self.count = 0

    def increment(self):
        with self.lock:      # 加锁确保原子性
            self.count += 1

    def get_count(self):
        return self.count
