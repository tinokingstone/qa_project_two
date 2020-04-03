import pytest
import app

def test_rand_str1():
    assert len(app.rand_str())==16 

def test_rand_str2():
    assert type(app.rand_int())==str


