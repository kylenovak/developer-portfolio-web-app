import random


class Characters(object):
    """Characters that make up a random key."""
    SYMBOLS = '!@#$%^&*()_+;,.[]-='
    NUMBERS = '1234567890'
    LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
    UPPERCASE_LETTERS = LOWERCASE_LETTERS.upper()

    @staticmethod
    def get_characters():
        return Characters.SYMBOLS + \
               Characters.NUMBERS + \
               Characters.LOWERCASE_LETTERS + \
               Characters.UPPERCASE_LETTERS


def contains_lowercase(key):
    """Checks a string for lowercase letters.
    Returns True if the string contains lowercase letters, False otherwise."""
    return len([s for s in key if s.islower()]) > 0


def contains_uppercase(key):
    """Checks a string for uppercase letters.
    Returns True if the string contains uppercase letters, False otherwise."""
    return len([s for s in key if s.isupper()]) > 0


def contains_numbers(key):
    """Checks a string for numbers.
    Returns True if the string contains numbers, False otherwise."""
    return len([s for s in key if s.isdigit()]) > 0


def contains_symbols(key):
    """Checks a string for symbols.
    Returns True if the string contains symbols, False otherwise."""
    return len([s for s in key if not s.isalnum()]) > 0


def strengthen_key(key):
    """Checks the strength of the key.
    Additional characters are added to the key if the key is weak."""
    if not contains_lowercase(key):
        key += random.choice(Characters.LOWERCASE_LETTERS)
    if not contains_uppercase(key):
        key += random.choice(Characters.UPPERCASE_LETTERS)
    if not contains_numbers(key):
        key += random.choice(Characters.NUMBERS)
    if not contains_symbols(key):
        key += random.choice(Characters.SYMBOLS)
    return key


def get_random_key(length=16):
    """Return a random string of characters for a given length."""
    key = ''.join([random.choice(Characters.get_characters()) for i in range(length)])
    return strengthen_key(key)

if __name__ == '__main__':
    print(get_random_key())
