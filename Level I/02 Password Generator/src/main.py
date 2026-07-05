from ctypes import py_object
import random
import string
import nltk
from abc import ABC, abstractmethod

nltk.download("words")


class PasswordGenerateor(ABC):
    @abstractmethod
    def generate(self):
        pass


class PinGenerator(PasswordGenerateor):
    def __init__(self, length: int = 8):
        self.length = length

    def generate(self) -> str:
        pin_str = map(str, [random.randrange(0, 10)
                      for _ in range(self.length)])
        return ''.join(pin_str)


class RandomPasswordGenerator(PasswordGenerateor):
    def __init__(self, length: int = 8, include_number: bool = False, include_symbols: bool = False):
        self.length = length
        self.charecter = string.ascii_letters
        if include_number:
            self.charecter += string.digits
        if include_symbols:
            self.charecter += string.punctuation

    def generate(self) -> str:
        return ''.join([random.choice(self.charecter) for _ in range(self.length)])


class MemorablePasswordGenerator(PasswordGenerateor):
    def __init__(self, num_of_words: int = 4, separator: str = '-', caplitalize: bool = False, vocabulary: list = None):
        if vocabulary is None:
            vocabulary = nltk.corpus.words.words()
        self.vocabulary = vocabulary
        self.num_of_words = num_of_words
        self.separator = separator
        self.caplitalize = caplitalize

    def generate(self):
        password_words = [random.choice(self.vocabulary)
                          for _ in range(self.num_of_words)]
        if self.caplitalize:
            password_words = [word.upper() if random.choice(
                [True, False]) else word.lower() for word in password_words]

        return self.separator.join(password_words)


if __name__ == "__main__":
    p_obj = PinGenerator(20)
    print(f"random pin: {p_obj.generate()}")
    w_obj = RandomPasswordGenerator(20, True, True)
    print(f"random password: {w_obj.generate()}")
    o_obj = MemorablePasswordGenerator(num_of_words=4, caplitalize=True)
    print(f"random password: {o_obj.generate()}")
