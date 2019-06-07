#!/usr/bin/python

import sys



def rock_paper_scissors(n):
  all_plays = []
  def loop_rps(n, plays=[]):
    if len(plays) >= n:
      all_plays.append([*plays])
    else:
      for i in range(3):
        plays_copy = [*plays]
        plays_copy.append(get_rps(i))
        loop_rps(n, plays_copy)

  loop_rps(n)
  return all_plays

def get_rps(i):
  plays = ["rock", "paper", "scissors"]
  return plays[i % 3]
  

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')

# Understand
#   Calculate all possible number of plays for n number of players in rock, paper, scissors.

# Plan
#   Right away this problem feels really redundant, which means there's a good way to optimize.  Each player can only make 3 possible plays
#   So I'm trying to calculate the number of calculates for 3 possible plays for n players.  For n=1, there are 3 plays.  For n=2, there are 9 plays.
#   In other words, the length of the array I returns should always be 3^n, which will be a good way to validate my answer.

#   To build the array, I need to build an array with a "rock, paper, scissors" entry for every player.

# n = 0  []
#             0        1            2
# n = 1  [["rock"], ["paper"], ["scissors"]]
#            0       0         0        1         0         2           1         0         1         1        1           2            2          0          2          1           2           2
# n = 1  [["rock", "rock"], ["rock", "paper"], ["rock", "scissors"], ["paper", "rock"], ["paper", "paper"], ["paper", "scissors"], ["scissors", "rock"], ["scissors", "paper"], ["scissors", "scissors"]]