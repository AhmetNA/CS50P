import sys
from jar import Jar

def test_jar():
    Jar(10).capacity == 10
    Jar(10).size == 0
    Jar(10).deposit(5)
    
def test_initial_capacity():
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0

def test_default_capacity():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0


