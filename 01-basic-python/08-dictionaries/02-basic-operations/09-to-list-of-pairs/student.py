def to_list_of_pairs(dictionary):
    result = []
    for k, v in dictionary.items():
        ans = (k, v)
        result.append(ans)
    return result
