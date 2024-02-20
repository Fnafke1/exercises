def median(ns):
    sorted_list = sorted(ns)
    if len(sorted_list) % 2 != 0:
        return sorted_list[len(sorted_list)//2]
    else:
        return (sorted_list[(len(sorted_list)//2) - 1] + sorted_list[(len(sorted_list)//2)]) / 2
