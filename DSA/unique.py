def is_unique(word):
    """ O(n) | dict.get() takes O(1) """
    word_dict = {}
    for c in word.lower():
        word_dict[c] = word_dict.get(c, 0) + 1
        if word_dict[c] > 1:
            return False
    return True


def is_unique_1(word):
    """ O(n^2) | slicing takes O(n) """
    word_lower = word.lower()
    rem_words = []
    ch = word_lower[0]
    for i in range(1, len(word_lower)):
        rem_words = word_lower[:i-1] + word_lower[i+1:]
        if ch in rem_words:
            return False
        else:
            ch = word_lower[i]
    return True


def is_unique_2(word):
    """ O(n) : similar to dict method but takes less space"""
    word = word.lower()
    if len(word) > 128:
        return False

    char_set = []
    for i in range(len(word)):
        val = ord(word[i]) - ord('a')
        if (char_set[val]):
            return False
        char_set[val] = True # cannot access unassigned memory in Python list
    return True


def is_unique_3(word):
    """ O(n*log(n)) """
    sorted_word = sorted(word)
    for i in range(1, len(sorted_word)):
        if sorted_word[i] == sorted_word[i-1]:
            return False
    return True


# -------------------------------------------------------------

my_words = ['Esmond', 'Adjei', 'School', 'Algorithm', 'Pharmacy']
for word in my_words:
    print(word, ''.join(['is unique' if is_unique_3(word) else 'not unique']))

