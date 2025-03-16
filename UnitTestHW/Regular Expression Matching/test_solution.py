import pytest
from solution import Solution  # 修正導入語法

@pytest.fixture
def solution():
    return Solution()

# 測試案例（s: 字串, p: 正則模式, expected_res: 預期結果）
testcases = [
    ("", "", True),
    ("aa", "a", False),
    ("aa", "a*", True),
    ("ab", ".*", True),
    ("a", ".*.", True),
    ("aab", "c*a*b", True),
    ("aaa", "ab*a*c*a", True)
]

@pytest.mark.parametrize("s, p, expected", testcases)
def test_ismatch(solution, s, p, expected):
    assert solution.isMatch(s, p) == expected

# 修正 xfail 測試案例，並補充參數
@pytest.mark.xfail
def test_broken_solution(solution):
    assert solution.isMatch() == True
