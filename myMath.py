import math


def isPrime(n):
  try:
    n=int(n)
    if n <= 1:
      return False
    if n == 2 or n == 3:
      return True
    if n % 2 == 0 or n % 3 == 0:
      return False
    
    for i in range(5, int(math.sqrt(n)) + 1, 6):
      if n % i == 0 or n % (i + 2) == 0:
        return False
    return True
  except:
    print("Invalid string")
    return None


def sum(start, end, step=1):
  try:
    l1=int(start)
    l2=int(end)
    if step=='':
      step=1
    step=abs(int(step))
    s=0
    if start>end:
      l1=end
      l2=start
    while l1<=l2:
      s+=l1
      l1+=step
    return s
  except:
    print("Invalid string")
    return None
  
