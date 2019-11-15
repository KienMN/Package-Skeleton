import pytest
from main_package.package_b import ClassB

def test_get_number():
  b = ClassB()
  assert b.get_number() == 2