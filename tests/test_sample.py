# Sample Test passing with nose and pytest

def test_pass():
    assert True, "dummy sample test"

from hidroteste.core import MyClass

def test_get_5():
    myclass = MyClass()
    assert myclass.get_5() == 5, "MyClass get_5 returns 5"
