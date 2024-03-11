def odd_keys_dict(dic):
    result = {}
    for k, v in dic.items():
        if k % 2 != 0:
            result[k] = v
    return result
