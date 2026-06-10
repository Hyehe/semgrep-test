import pytest
from vulnerable_sample import hash_password, divide, get_username

def test_hash_password():
    result = hash_password("admin1234")
    assert result is not None
    assert len(result) == 32

def test_divide_normal():
    assert divide(10, 2) == 5.0

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

def test_get_username_none():
    with pytest.raises((TypeError, KeyError)):
        get_username(None)