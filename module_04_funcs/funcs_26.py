def printfunction(args, fun):
    for x in args:
        print(f'f({x}) = {fun(x)}', sep=', ')


def poly(x):
    return 2 * x ** 2 - 4 * x + 2


print(poly)
printfunction([x for x in range(-2, 3)], poly)


