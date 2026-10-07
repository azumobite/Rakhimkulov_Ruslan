def count_vowels(s):
  alph = set("aeiou")
  return sum(1 for x in s.lower() if x in alph)

def has_unique_characters(s):
  return len(set(s)) == len(s)

def count_one_bits(n):
  return bin(n).count("1")

def multiplicative_persistence(n):
  count = 0
  while n >= 10:
    x = 1
    for y in str(n):
      x *= int(y)
    n = x
    count += 1
  return count

def mse(x, y):
  return sum((xi - yi) ** 2 for xi, yi in zip(x, y)) / len(x)

def prime_factorization(n):
  factors = {}
  d = 2
  while d * d <= n:
    while n % d == 0:
      factors[d] = factors.get(d, 0) + 1
      n //= d
    d += 1
  if n > 1:
    factors[n] = factors.get(n, 0) + 1

  result = ""
  for prime in sorted(factors.keys()):
    power = factors[prime]
    if power == 1:
      result += f"({prime})"
    else:
      result += f"({prime}**{power})"
  return result

def pyramid(n):
  k = 1
  current_sum = 0
  while current_sum < n:
    current_sum += k * k
    if current_sum == n:
      return k
    k += 1
  return "It is impossible"

def is_balanced_number(n):
  s = str(n)
  length = len(s)
  mid = length // 2
  if length % 2 == 0:
    left_part, right_part = s[:mid], s[mid:]
  else:
    left_part, right_part = s[:mid], s[mid + 1 :]
  return sum(int(c) for c in left_part) == sum(int(c) for c in right_part)
