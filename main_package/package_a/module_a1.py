from .utils import hello_a

class ClassA():
  def __init__(self):
    self._number = 1
    
  def hello(self):
    hello_a()

  def get_number(self):
    return self._number