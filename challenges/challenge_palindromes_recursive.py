def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0:
        return False
    if len(word) == 1:
        return True
    if len(word) == 2:
        return word[0] == word[1]
    if word[0] != word[-1]:
        return False
    return is_palindrome_recursive(word[1:-1], low_index, high_index)
