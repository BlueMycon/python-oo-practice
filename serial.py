class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__ (self, start):
        """Establishes starting point and saved place in count"""
        self.start = self.count = start

    def generate (self):
        """Increments self.count by 1 and returns self.count"""
        self.count += 1
        return self.count -1

    def reset (self):
        """Resets count back to self.start value"""
        self.count = self.start