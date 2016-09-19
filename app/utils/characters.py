

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

    @staticmethod
    def contains_lowercase(chars):
        """Checks a string for lowercase letters.
        Returns True if the string contains lowercase letters, False otherwise."""
        return len([c for c in chars if c.islower()]) > 0

    @staticmethod
    def contains_uppercase(chars):
        """Checks a string for uppercase letters.
        Returns True if the string contains uppercase letters, False otherwise."""
        return len([c for c in chars if c.isupper()]) > 0

    @staticmethod
    def contains_numbers(chars):
        """Checks a string for numbers.
        Returns True if the string contains numbers, False otherwise."""
        return len([c for c in chars if c.isdigit()]) > 0

    @staticmethod
    def contains_symbols(chars):
        """Checks a string for symbols.
        Returns True if the string contains symbols, False otherwise."""
        return len([c for c in chars if not c.isalnum()]) > 0
