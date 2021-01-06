class EvenNumbers(object):
    def __init__(self, maximum):
        self.maximum = maximum

    def __iter__(self):
        return EvenIterator(self)

class EvenIterator(object):
    def __init__(self, container):
        self.container = container
        self.n = 0

    def __next__(self):
        self.n += 2
        if self.n > self.container.maximum:
            raise StopIteration
        return self.n

    def __iter__(self):
        return self


numbers = EvenNumbers(10)
for num in numbers:
    print(num)
