#!/usr/bin/python

import sys

coins = [1,5,10,25,50]
def making_change(amount, coins=coins):
  outcomes = [0 for k in range(amount + 1)]
  # outcomes is a measure of how many ways each amount can be created given the currency
  outcomes[0] = 1
  for i in range(0,len(coins)):
    for j in range(coins[i],amount + 1):
      # Loop over outcomes and add in previously calculated amounts to the current
      outcomes[j] += outcomes[j - coins[i]]
  return outcomes[amount]
    

making_change(10)


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    coins = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, coins), amount=amount))
  else:
    print("Usage: making_change.py [amount]")