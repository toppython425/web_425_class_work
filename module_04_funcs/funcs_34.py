def make_closer(par):
    loc = par  # loc = 2

    def power(inner_par1):
        return inner_par1 ** loc  # loc == 2

    return power


f_square = make_closer(2)
# def power(inner_par1), loc == 2:
f_cube = make_closer(3)
# def power(inner_par1), loc == 3:

for i in range(5):
    print(f"{i} - квадрат {f_square(i)}; куб {f_cube(i)}")
