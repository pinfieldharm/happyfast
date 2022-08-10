import sys


# Two optimizations
# - (new) Sort digits before computations / caching (since order isn't important for square sum)
# - (from set_happy.py) Cache happy / unhappy results
#
# Sorting digits reduces time by about half.

# 20:16 $ time python sort_set_happy.py 1000000
# 143071
#
# real    0m1.632s
# user    0m1.553s
# sys     0m0.034s
def happy(max_number):
    known_happy = {1}
    known_unhappy = set()
    return sum(1 for _ in filter(lambda x: is_happy(x, set(), known_happy, known_unhappy), range(1, max_number + 1)))


def is_happy(x, seen, known_happy, known_unhappy):
    current = sorted_num(x)
    while current not in seen and current not in known_happy and current not in known_unhappy:
        seen.add(current)
        current = sorted_num(digit_square_sum(current))

    if current == 1:
        known_happy.update(seen)
        return True
    elif current in known_happy:
        known_happy.update(seen)
        return True
    else:
        known_unhappy.update(seen)
        return False


def sorted_num(x):
    return int("".join(sorted(list(str(x)))))


def digit_square_sum(x):
    return sum([int(d) ** 2 for d in str(x)])


if __name__ == '__main__':
    print(happy(int(sys.argv[1])))
