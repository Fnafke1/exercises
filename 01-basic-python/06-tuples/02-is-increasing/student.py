def is_increasing(ns):
    for i in range(1, len(ns)):
        if ns[i-1] > ns[i]:
            return False
    return True


print(is_increasing([1, 2, 2, 4, 6, 6, 10]))
