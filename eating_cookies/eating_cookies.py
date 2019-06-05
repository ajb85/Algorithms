#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  if n == 0:
    return 1
  elif n < 0:
    return 0
  cache = {} if cache == None else cache
  if not n in cache:
    cache[n] = eating_cookies(n-3) + eating_cookies(n-2) + eating_cookies(n-1)

  return cache[n]

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')


    # 1. Determine how many different ways cookie monster can eat n numbers of cookies, knowing that he can either eat 3, 2, or 1 cookies in a given "cycle"

    # 2. This is definitely a recursion problem.  However, because each cycle has the possibility to generate up to 3 separate instances of the function, 
    # optimization is going to be really important.  I suspect 3*2*1 will give me a number where anything more than that will just be repeats of the same data.
    # So rather than caching the values, I want to know the number of possibilities of 3*2*1 cookies, find the number of times n can be evenly divided by 3*2*1, and
    # multiply that number by the possibilities.  The remainder can go into the recursive function.  That puts my worst case scenario at roughly n = 5 --> 15 iterations
