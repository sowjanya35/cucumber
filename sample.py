import pytest

@pytest.fixture()
def setUp():
    print("basic")

def test_A(setUp):
    print("method A")
print('hello world........')

