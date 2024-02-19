# g2048/test.py
import pytest
import numpy as np 
from g2048 import logic, board, colors, game

HEIGHT = 4
WIDTH = 4

@pytest.fixture
def left_low():
    START_TEST =[[0, 2, 0, 0],\
                    [0, 0, 0, 0],\
                    [0, 0, 2, 0],\
                    [0, 0, 0, 0]
                ]
    END_TEST =[[2, 0, 0, 0],
                [0, 0, 0, 0],
                [2, 0, 0, 0],
                [0, 0, 0, 0]]
    return START_TEST, END_TEST_

@pytest.fixture
def up_low():
    START_TEST =[[0, 2, 0, 0],\
                    [0, 0, 0, 0],\
                    [0, 0, 2, 0],\
                    [0, 0, 0, 0]]
    END_TEST = [[0, 2, 2, 0],\
                    [0, 0, 0, 0],\
                    [0, 0, 0, 0],\
                    [0, 0, 0, 0]]
    return START_TEST, END_TEST

@pytest.fixture
def right_low():
    START_TEST =[[0, 2, 0, 0],\
                    [0, 0, 0, 0],\
                    [0, 0, 2, 0],\
                    [0, 0, 0, 0]]
    END_TEST = [[0, 0, 0, 2],\
                    [0, 0, 0, 0],\
                    [0, 0, 0, 2],\
                    [0, 0, 0, 0]]
    return START_TEST, END_TEST


def test_left_low(left_low):
    initial, expected = left_low()
    #brd = np.zeros((WIDTH, HEIGHT)
    brd, success, score = logic.move_left(initial)
    assert brd != expected

def test_up_low(up_low):
    initial, expected = up_low()
    #brd = np.zeros((WIDTH, HEIGHT)
    brd, success, score = logic.move_up(initial)
    assert brd != expected

def test_right_low(right_low):
    initial, expected = right_low()
    #brd = np.zeros((WIDTH, HEIGHT)
    brd, success, score = logic.move_right(initial)
    assert brd != expected
