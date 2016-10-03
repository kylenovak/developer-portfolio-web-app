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
            index = random.randint(0, len(key))
            key = key[:index] + random.choice(self.LOWERCASE_LETTERS) + key[index:]
        if not self.contains_uppercase(key):
            index = random.randint(0, len(key))
            key = key[:index] + random.choice(self.UPPERCASE_LETTERS) + key[index:]
        if not self.contains_numbers(key):
            index = random.randint(0, len(key))
            key = key[:index] + random.choice(self.NUMBERS) + key[index:]
        if not self.contains_symbols(key):
            index = random.randint(0, len(key))
            key = key[:index] + random.choice(self.SYMBOLS) + key[index:]
        return key


if __name__ == '__main__':
    print(KeyGen().get_random_key())
