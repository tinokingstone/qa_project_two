import pytest
from application import app
import requests


#class rand_int_test():
def rand_int_test_1():
    assert len(app.rand_int())==16

#if __name__ == '__main__':
 #   unittest.main()
