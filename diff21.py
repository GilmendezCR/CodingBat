#Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.

#diff21(19) → 2
#diff21(10) → 11
#diff21(21) → 0

def diff21(n):
  diff = 21 - n
  double = (n - 21) * 2
  if n <= 21:
    return diff
  elif n > 21:
    return double

diff21(19) 
diff21(10) 
diff21(21) 