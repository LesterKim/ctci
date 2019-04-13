def add_parens(n):
  if n == 0:
    return []
  if n == 1:
    return ['()']

  lefts = 0
  rights = 0

  for i in range(2*n):
    if lefts == rights:
      s = s + '('
    else:



def parens(n):
  if n == 0:
    return {}
  if n == 1:
    return {'()': None}

  p_hash = dict()

  for p_str in parens(n-1):
    for j in range((len(p_str) >> 1) + 1):
      new_s = p_str[:j] + '()' + p_str[j:]

      if new_s not in p_hash:
        p_hash[new_s] = None

  return p_hash

n = 4
for p in parens(n):
  print(p)
