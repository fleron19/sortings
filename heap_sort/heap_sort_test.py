from .heap_sort import heap_sort
import pytest
import random


@pytest.fixture
def random_list():
    return random.sample(range(1, 1000001), random.randint(1, 100))

@pytest.mark.parametrize(
    ["n", "expected"],
    [([1], [1]),
     ([2, 7, 4, 8, 6, 5], [2, 4, 5, 6, 7, 8]),
     ([], []),
     ([9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
     ([1, 3, 2, 3, 1], [1, 1, 2, 3, 3])]
)
def test_heap_sort_main(n, expected):
    assert heap_sort(n) == expected

def test_heap_sort_random(random_list):
    assert heap_sort(random_list) == list(sorted(random_list))

rand_tests = []
for i in range(10):
    rand_list = random.sample(range(1, 1000001), random.randint(1, 100))
    tup = (rand_list, sorted(rand_list))
    rand_tests.append(tup)

@pytest.mark.parametrize(
    ["n", "expected"],
    rand_tests
)
def test_heap_sort_multiple(n, expected):
    assert heap_sort(n) == expected
