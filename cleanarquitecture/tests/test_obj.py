import pytest
from unittest import mock
from cleanarquitecture.example import MyObj

def test_connect():
    external_obj = mock.Mock()
    MyObj(external_obj)
    external_obj.connect.assert_called_with()

def test_setup():
    external_obj = mock.Mock()
    obj = MyObj(external_obj)
    obj.setup()
    external_obj.setup.assert_called_with(cache=True)