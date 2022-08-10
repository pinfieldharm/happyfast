import sys


# One optimization
# - (new) Sort digits before computations / caching (since order isn't important for square sum)
#
# Caching reduces run time by about 90%
#
# 13:27 $ time python set_happy.py 1000000
# 143071
#
# real    0m3.575s
# user    0m3.511s
# sys     0m0.054s
def happy(max_number):
    known_happy = {1}
    known_unhappy = set()
    return sum(1 for _ in filter(lambda x: is_happy(x, set(), known_happy, known_unhappy), range(1, max_number + 1)))


def is_happy(x, seen, known_happy, known_unhappy):
    current = x
    while current not in seen and current not in known_happy and current not in known_unhappy:
        seen.add(current)
        current = digit_square_sum(current)

    if current == 1:
        known_happy.update(seen)
        return True
    elif current in known_happy:
        known_happy.update(seen)
        return True
    else:
        known_unhappy.update(seen)
        return False


def digit_square_sum(x):
    return sum([int(d) ** 2 for d in str(x)])


if __name__ == '__main__':
    print(happy(int(sys.argv[1])))
