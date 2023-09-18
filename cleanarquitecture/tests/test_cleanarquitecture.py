#!/usr/bin/env python

"""Tests for `cleanarquitecture` package."""

import pytest

from cleanarquitecture.Calc import Calc 


def test_add_two_numbers():
    c = Calc()
    res = c.add(9,4,2)    
    assert res == 15


def test_add_many_numbers():
    s = range(100)
    assert Calc().add_mn(*s) == 4950

def test_substract_two_number():
    assert Calc().sub(9,4) == 5


def test_mul_two_number():
    assert Calc().mul(3,5,4) == 60

def test_mult_many_numbers():
    s = range(1,10)
    assert Calc().mul(*s)==362880

def test_div_two_numbers_float():
    c = Calc()
    res = c.div(13,2)
    assert res == 6.5

def test_div_zero_returns_inf():
    c = Calc()
    res = c.div(5,0)
    assert res == "inf"


def test_mul_by_zero_raises_exception():
    c = Calc()
    with pytest.raises(ValueError):
        c.mul(3,0)

def test_correct_average():
    c = Calc()  
    res =  c.avg([2,5,12,98])
    assert res==29.25


def test_avg_removes_upper_outliers():
    c = Calc()
    res = c.avg([2,5,12,98], ut=90)    
    assert  res == pytest.approx(6.333333)

def test_avg_removes_lowe_outliers():
    c = Calc()
    res = c.avg([2,5,12,98], lt=10)
    assert res == pytest.approx(55)

def test_avg_empty_list():
    c = Calc()
    res = c.avg([])
    assert res == pytest.approx(0)

def test_avg_manages_empty_list_before_outlier_removal():
    c = Calc()
    res = c.avg([], lt=15, ut=90)
    assert res == 0

def test_avg_manages_zero_value_lower_outlier():
    c = Calc()
    res = c.avg([-1, 0, 1], lt=0)
    assert res == 0.5

def test_avg_manages_zero_value_upper_outlier():
    c = Calc()
    res = c.avg([-1, 0, 1], ut=0)
    assert res == -0.5