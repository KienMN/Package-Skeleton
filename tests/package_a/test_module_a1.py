import pytest
from main_package.package_a import ClassA

def test_get_number():
  a = ClassA()
  assert a.get_number() == 1