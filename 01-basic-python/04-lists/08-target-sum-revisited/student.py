def target_sum(ns, target):
    index_outer = 0
    index_inner = 0
    for i in range(len(ns)):
        index_outer += 1
        for j in range(len(ns)):
            index_inner += 1
            if index_inner != index_outer:
                if ns[i] + ns[j] == target:
                    return True
            if index_inner == len(ns):
                index_inner = 0
                pass
    return False
