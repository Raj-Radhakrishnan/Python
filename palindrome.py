def is_palindrome(word):
    reversed = word[::-1]
    if reversed.upper() == word.upper():
        return True
    else:
        return False

print(is_palindrome('Deleveled'))