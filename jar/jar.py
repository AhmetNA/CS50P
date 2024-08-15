class Jar:
    def __init__(self, capacity=12):
        try:
            if capacity < 0:
                raise ValueError("Capacity must be a positive integer")
        except ValueError as e:
            print("Error", e)
            capacity = 12
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪"*self.size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Jar is full")
        self.size += n

    def withdraw(self, n):
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, n):
        self._size = n


def main():
    jar = Jar(10)
    jar.deposit(5)
    jar.withdraw(2)
    print(jar)

if __name__ == "__main__":
    main()
