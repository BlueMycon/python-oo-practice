from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary.

    >>> wf = WordFinder("/usr/share/dict/words")
    235886 words read

    >>> 


    """

    def __init__(self, path):
        """Opens file, initializes words list, parses file, prints words count"""
        file = open(path)
        self.words = self.parse(file)
        self.print_count()

    def parse(self, file):
        """line by line, strips whitespace and \n, and appends line to words list"""
        return [line.strip() for line in file]

    def print_count(self):
        """Print number of words in list"""
        print(f"{len(self.words)} words read")

    def random(self):
        """Return a random word"""
        return choice(self.words)

class SpecialWordFinder(WordFinder):
    """Special Word Finder: Word Finder that ignores comments and blank lines"""

    def parse(self, file):
        """line by line, removes comment lines and \n,
           strips whitespace and \n, and appends line to words list"""
        return [line.strip() for line in file if not line.startswith(("#", "\n"))]
