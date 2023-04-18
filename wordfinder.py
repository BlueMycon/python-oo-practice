from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, path):
        """Opens file, initializes words list, parses file, prints words count"""
        self.file = open(path)
        self.words = []
        self.parse()
        self.print_count()

    def parse(self):
        """line by line, strips whitespace and \n, and appends line to words list"""
        for line in self.file:
            self.parse_line(line)

    def parse_line(self, line):
        """Parse individual line and append to list"""
        line.strip()
        line = line[:len(line) - 1]
        self.words.append(line)

    def print_count(self):
        """Print number of words in list"""
        print(f"{len(self.words)} words read")

    def random(self):
        """Return a random word"""
        return choice(self.words)

class SpecialWordFinder(WordFinder):
    """Special Word Finder: finds a random word from a special dictionary"""

    def __init__(self, path):
        """Parent init opens file, initializes words list, parses file, prints words count"""
        super().__init__(path)

    def parse(self):
        """line by line, removes comment lines and \n,
           strips whitespace and \n, and appends line to words list"""
        for line in self.file:
            if line[0] == "#" or line[0] == "\n":
                continue
            else:
                super().parse_line(line)

    def print_count(self):
        """Print number of words in list"""
        return super().print_count()

    def random(self):
        """Return a random word"""
        return super().random()

