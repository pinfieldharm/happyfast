#!/usr/bin/env bash

# Force one-line time output
TIMEFORMAT=$'real\t%3lR\tuser\t%3lU\tsys\t%3lS'

# Default max number to one million
MAX_NUMBER="${1:-1000000}"

set -x
time python happy.py $MAX_NUMBER
time python c_happy.py $MAX_NUMBER
time python c_two_stage_happy.py $MAX_NUMBER
time python set_happy.py $MAX_NUMBER
time python sort_set_happy.py $MAX_NUMBER
time python c_ext_happy.py $MAX_NUMBER
