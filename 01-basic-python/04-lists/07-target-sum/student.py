def target_sum(ns, target):
    for item in range(len(ns)):
        for compare in range(len(ns)):
            if ns[item] + ns[compare] == target:
                return True
    return False
