# a^3 + b^3 = c^3 + d^3
n = 1000
cubes = []
dic = {}

for c in range(1,n):
  for d in range(c+1,n):
    e = c**3 + d**3

    if e in dic:
      dic[e].append([c,d])
    else:
      dic[e] = [[c,d]]

for a in range(1,n):
  for b in range(a+1,n):
    f = a**3 + b**3

    if f in dic:
      for pair in dic[f]:
        if pair != [a,b]:
          cubes.append([a,b] + pair)
       # d = int((i**3 + j**3 - k**3) ** (1/3))

      #  if i**3 + j**3 == k**3 + d**3:
     # cubes.append([i,j,k,d])

for cube in cubes:
  print(cube)
