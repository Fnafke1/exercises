def remove_duplicates(xs):
    found = set()
    result = []
    for i in xs:
        if i not in found:
            result.append(i)
            found.add(i)
    return result
