class StringOperations:
    @staticmethod
    def reverse(s):
        return s[::-1]

    @staticmethod
    def is_palindrome(s):
        s = s.lower().replace(" ", "")
        return s == s[::-1]

    @staticmethod
    def count_vowels(s):
        vowels = "aeiou"
        return sum(1 for char in s.lower() if char in vowels)
