def keys_with_value(dic, value):
    result = []
    for k, v in dic.items():
        if v == value:
            result.append(k)
    return result
