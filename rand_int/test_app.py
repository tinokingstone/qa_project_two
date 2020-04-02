import pytest
import app
    #import requests


#class Test_rand_int():
def test_rand_int1():
    assert len(app.rand_int())==16 

def test_rand_int2():
    assert type(app.rand_int())==str

#if __name__ == '__main__':
 #   unittest.main()
