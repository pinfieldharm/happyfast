import sys


# Basic solution, no optimizations

# 09:38 $ time python happy.py 1000000
# 143071
#
# real    0m20.763s
# user    0m20.664s
# sys     0m0.063s

def happy(max_number):
    return sum(1 for _ in filter(lambda x: is_happy(x), range(1, max_number + 1)))


def is_happy(x):
    seen = []
    current = x
    while current not in seen:
        seen.append(current)
        current = digit_square_sum(current)

    return current == 1


def digit_square_sum(x):
    return sum([int(d) ** 2 for d in str(x)])


if __name__ == '__main__':
    print(happy(int(sys.argv[1])))
