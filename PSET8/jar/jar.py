class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Invalid capacity")
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if (self.size + n) > self.capacity:
            raise ValueError("Invalid deposit")
        self.size += n
        return self.size

    def withdraw(self, n):
        if (self.size - n) < 0:
            raise ValueError("Invalid withdraw")
        self.size -= n
        return self.size

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @size.setter
    def size(self, size):
        self._size = size
