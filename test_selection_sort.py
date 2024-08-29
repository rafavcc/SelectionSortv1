import pytest
import numpy as np
from SelectionSort import *

def test_small():
    random_list_1 = [19, 22, 33, 11, 1]
    sorted_list_1 = sorted(random_list_1)
    selected_list_1 = bubble_sort(random_list_1)
    assert sorted_list_1 == selected_list_1

def test_reverse():
    reverse_list_1 = [ 7, 5, 6, 4, 3, 2, 1]
    sorted_list_1 = sorted(reverse_list_1)
    selected_list_1 = bubble_sort(reverse_list_1)
    assert sorted_list_1 == selected_list_1
    
def test_random():
    random_list = np.random.randint(0,4200, size = 30).tolist()
    sorted_list_1 = sorted(random_list)
    selected_list_1 = bubble_sort(random_list)
    assert sorted_list_1 == selected_list_1