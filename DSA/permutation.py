def are_perm(string1, string2):
    '''
    Compares if two strings are permutations of the other.
    Takes O(n*log(n)) because of sort.
    Note: it's case and whitespace sensitive.
    '''
    if len(string1) != len(string2):
        return False

    return sorted(string1) == sorted(string2)


def are_perm2(string1, string2):
    '''
    compares if one string is the perm of the other.
    Should take O(n). 
    Note: it's case and whitespace sensitive
    '''
    str_len = len(string1)
    if str_len != len(string2):
        return False

    str1_sum, str2_sum = 0, 0
    for i in range(str_len):
        str1_sum += ord(string1[i])
        str2_sum += ord(string2[i])

    return str1_sum == str2_sum


if __name__ == "__main__":
    str1 = "God" #'esmond'
    str2 = "dog" #'domens'
    print(str1, str2, are_perm2(str1, str2))
