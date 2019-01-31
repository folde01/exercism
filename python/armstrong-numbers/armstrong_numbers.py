def is_armstrong(number):
  num_str = str(number)
  exponent = len(num_str)
  num_str_rev = num_str[::-1]
  total = 0

  for c in num_str_rev:
    digit = int(c)
    total += digit ** exponent

  return total == number
