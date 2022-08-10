import sys
from happyc import digit_square_sum


# Basic solution, with c for squaring and summing digits

# 19:00 $ time python c_happy.py 1000000
# 143071
#
# real    0m3.460s
# user    0m3.424s
# sys     0m0.025s
def happy(max_number):
    return sum(1 for _ in filter(lambda x: is_happy(x), range(1, max_number + 1)))


def is_happy(x):
    seen = set()
    current = x
    while current not in seen:
        seen.add(current)
        current = digit_square_sum(current)

    return current == 1


if __name__ == '__main__':
    print(happy(int(sys.argv[1])))
