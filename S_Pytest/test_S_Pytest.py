# coding:utf-8
import pytest


def func(x):
    return x + 1


def test_func():
    assert func(2) == 3


if __name__ == "__main__":
    pytest.main("-q --html=a.html")
