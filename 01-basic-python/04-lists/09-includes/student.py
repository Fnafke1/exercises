def includes(xs, ys):
    included = True
    for i in ys:
        if i in xs:
            included = True
        else:
            included = False
    return included
