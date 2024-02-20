def word_count(string):
    if len(string) == 0:
        return 0

    split_string = string.split(' ')

    return len(split_string)
