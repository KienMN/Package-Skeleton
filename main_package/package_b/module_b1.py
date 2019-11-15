from ..package_a import ClassA

class ClassB(ClassA):
  def __init__(self):
    super().__init__()

  def hello(self):
    print('Hello B', end=' ')
    super().hello()

  def get_number(self):
    self._number += 1
    return super().get_number()
    