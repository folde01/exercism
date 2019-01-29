import string

def is_pangram(sentence):
  alphabet = string.ascii_lowercase  
  seen = set() 
  for char in sentence:
    lowered = char.lower()
    if lowered in alphabet: 
      seen.add(lowered)
    if len(seen) == 26:
      return True 
  return False
