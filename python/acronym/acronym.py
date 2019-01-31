import re

def abbreviate(words):
  word_list = re.split('\s+|-', words)
  first_chars = [ word.replace('_', '')[0:1].upper() for word in word_list ] 
  acronym = ''.join(first_chars) 
  return acronym
