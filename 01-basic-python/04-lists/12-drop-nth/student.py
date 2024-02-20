def drop_nth(xs, n):
    ys = []
    for i in range(len(xs)):
        if i != n:
            ys.append(xs[i])
    return ys
