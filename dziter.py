
class EvenNumbers:

    def __init__(self, start=0, end=1):
        self.start = start
        self.end = end

    def __iter__(self):
        self.start = self.start - 1
        return self

    def __next__(self):
        while self.start < self.end:
            self.start += 1
            if self.start % 2 == 0:
                return self.start
        else:
            raise StopIteration()

en = EvenNumbers(10, 25)
for i in en:
    print(i)

