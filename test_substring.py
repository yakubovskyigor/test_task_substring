import pytest

from substring import substring


@pytest.mark.parametrize(
    "s, k, expected", (
        ("abcdef", 2, 2),
        ("aaaaa", 2, 5),
        ("abaccab", 2, 4)
    )
)
def test_substring(s, k, expected):
    assert substring(s, k) == expected