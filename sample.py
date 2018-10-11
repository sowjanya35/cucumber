import pytest

@pytest.fixture()
def setUp():
    print("basic")

def test_A(setUp):
    print("method A")
 def test_B(setUp):
    print("method B")
print('hello world........')

