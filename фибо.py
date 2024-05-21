class FibonacciIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0
        self.previous = 0
        self.next = 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.limit:
            raise StopIteration

        if self.count == 0:
            self.count += 1
            return self.previous
        elif self.count == 1:
            self.count += 1
            return self.next
        else:
            self.count += 1
            fib_number = self.previous + self.next
            self.previous = self.next
            self.next = fib_number
            return fib_number