def add_indices(xs):
    ys = []
    for i in range(len(xs)):
        ys.append(i)
    return list(zip(ys, xs))
