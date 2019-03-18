dic = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
    1000: 'thousand',
    1000000: 'million' }


def to_english(n):
  s = []

  count = 0

  while n > 0:
    last_d = n % 1000

    if last_d % 100 <= 20:
      s.append(dic[last_d])
    else:
      ones = last_d % 10
      if ones > 0:
        s.append(dic[ones])

      tens = last_d // 10 % 10
      s.append(dic[10 * tens])

    huns = last_d // 100

    if huns > 0:
      s.extend([dic[100], dic[huns]])

    n //= 1000
    count += 3

    if count == 3:
      s.append(dic[1000])
    if count == 6:
      s.append(dic[1000000])

  return ' '.join(s[::-1])

n = 123456789
s = 'one hundred twenty three million four hundred fifty six thousand seven hundred eighty nine'

print(to_english(n) == s)
