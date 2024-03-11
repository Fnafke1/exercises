def merge_dicts(dic1, dic2):
    result = {}
    for k, v in dic1.items():
        result[k] = v
    for k, v in dic2.items():
        result[k] = v
    return result
