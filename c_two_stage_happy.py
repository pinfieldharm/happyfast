import sys
from happyc import digit_square_sum

# with c extension plus precomputing main bits

# 21:24 $ time python c_two_stage_happy.py 1000000
# 143071
#
# real    0m0.241s
# user    0m0.222s
# sys     0m0.015s
MAX_INPUT = 1999999999999999999


def happy(max_number):
    precomputed = precompute(digit_square_sum(MAX_INPUT))
    return sum(1 for _ in filter(lambda x: precomputed[digit_square_sum(x)], range(1, max_number + 1)))


def precompute(max_number):
    return list(map(lambda x: is_happy(x), range(0, max_number + 1)))


def is_happy(x):
    seen = set()
    current = x
    while current not in seen:
        seen.add(current)
        current = digit_square_sum(current)

    return current == 1


if __name__ == '__main__':
    print(happy(int(sys.argv[1])))
