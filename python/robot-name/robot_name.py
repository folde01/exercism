import string, random, os

class Robot(object):
  def __init__(self):
    self.name = ''
    self.reset()
  def reset(self): 
    random_from_os = int.from_bytes(os.urandom(4), byteorder='big')
    random.seed(random_from_os)
    self.name = ''
    for i in range(0, 2):
      self.name += random.choice(string.ascii_uppercase)
    for i in range(0, 3):
      self.name += str(random.randint(0, 9))
