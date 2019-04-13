def recursive_mult(a, b):
  if b == 0: return b
  if b == 1: return a

  val = a if b%2 == 1 else 0

  return val + (recursive_mult(a, b >> 1) << 1)

a = 75
b = 75

print(recursive_mult(a,b) == a*b)
