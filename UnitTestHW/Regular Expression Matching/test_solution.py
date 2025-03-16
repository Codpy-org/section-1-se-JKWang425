import pytest
from solution import pytest

@pytest.fixture
def solution():
    class Wrapper:
        def isMatch(self, s, p):
            return isMatch(s, p)
    return Wrapper()
    
testcases = [
    # s, p, expected_res
    ["", "", True],
    ["aa", "a", False],
    ["aa", "a*", True],
    ["ab", ".*", True],
    ["a", ".*.", True],
    ["aab", "c*a*b", True],
    ["aaa", "ab*a*c*a", True]
]

@pytest.mark.parametrize([?], testcases)
...
    assert solution.isMatch(s, p) == expected


@pytest.mark.xfail
def test_broken_solution(solution):
    assert solution.isMatch() == 
