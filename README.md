# Getting Happy Faster with Python

This repo contains some simple experiments in speeding up the computation of Happy Numbers 
(see https://en.wikipedia.org/wiki/Happy_number for a good description of these). The short version 
of this is a happy number is one where repeated summing of the squares of the digits of the number reaches 1.

This was used for an informal tech talk a few years ago.

## Setup

These are known to run with python 3.8. I'd suggest using virtualenv or similar.

Some of the implementations use a c extension (happyc.c), which you'll first need to build and install.

```bash
python setup.py build
python setup.py install
```

All are invoked `python <script name> <n>` where `n` is the max integer for happiness. For easier performance
testing, these just print out the count of happy numbers, rather than the list itself.

Alternatively, you can use `runall.sh` to run all of the scripts on the same input and see the timing.

## The good experiments

`happy.py` is the basic python solution. It takes about 20s to compute all the happy numbers up to one million on
my laptop. It does this by just looping and computing happiness independently for each input. 

`c_happy.py` uses a C extension to calculate sums of squares of digits, and computes up to one million in about 3s.

`c_two_stage_happy.py` uses the observation that, up to the limit of a 32-bit int (which seems big enough!), any starting number will reduce
down to a 4-digit number equal to or less than 1459 (the sum of squared digits for 1999999999999999999). So it computes
the happiness of 1 through 1459 and caches the results. Computation of happiness then reduces to finding the first 
sum of squared digits and then looking it up in the cache. This computes happy numbers up to one million in 0.2 seconds.

## The other experiments

The above was the most successful set of optimizations. Prior to those, I made some attempts based on just caching all 
computational results. These got very memory-intensive at large numbers. This wasn't a total waste though, because doing these
ones led me to the realization that the number of results to cache could actually be pretty small 
(see comment about `c_two_stage_happy` above.)

`set_happy.py` caches all happy and unhappy results in a couple of sets. Took about 4s.

`sort_set_happy.py` extends the above by normalizing numbers by sorting their digits, so that combinations 
of the same digits aren't all computed. Took about 1.6s.

    `c_ext_happy.py` extends the above by doing the digit sorting in c. This got down to about 0.6 seconds to compute up to 
one million, and then was very hard to find a path to getting any better performance.

