def digit_sum(x):
    string_num = str(x)
    count = 0
    for i in range(len(string_num)):
        count += int(string_num[i])
    return count


def last_digit(x):
    return int(str(x)[-1])


def remove_last_digit(x):
    if len(str(x)) == 1:
        return 0
    return int(str(x)[0:-1])
