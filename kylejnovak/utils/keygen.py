import random
from .characters import Characters


class KeyGen(Characters):
    def get_random_key(self, size=16):
        """Return a random string of characters for a given size."""
        key = ''.join([random.choice(Characters.get_characters()) for i in range(size)])
        return self.__strengthen_key(key)

    def __strengthen_key(self, key):
        """Checks the strength of the key.
        Additional characters are added to the key if the key is weak."""
        if not self.contains_lowercase(key):
            key += random.choice(self.LOWERCASE_LETTERS)
        if not self.contains_uppercase(key):
            key += random.choice(self.UPPERCASE_LETTERS)
        if not self.contains_numbers(key):
            key += random.choice(self.NUMBERS)
        if not self.contains_symbols(key):
            key += random.choice(self.SYMBOLS)
        return key


if __name__ == '__main__':
    print(KeyGen().get_random_key())
