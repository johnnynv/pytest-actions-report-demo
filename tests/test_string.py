import pytest
from pytestshow.string_ops import StringOperations


@pytest.mark.fast
@pytest.mark.positive
class TestStringBasicOperations:
    def test_reverse(self, string_ops):
        assert string_ops.reverse("hello") == "olleh"

    def test_count_vowels(self, string_ops):
        assert string_ops.count_vowels("hello") == 2


@pytest.mark.slow
@pytest.mark.positive
class TestStringAdvancedOperations:
    @pytest.mark.parametrize(
        "input_str,expected", [("madam", True), ("racecar", True), ("hello", False)]
    )
    def test_is_palindrome(self, string_ops, input_str, expected):
        assert string_ops.is_palindrome(input_str) == expected


@pytest.mark.negative
def test_empty_string(string_ops):
    assert string_ops.reverse("") == ""


@pytest.mark.smoke
def test_smoke_string():
    assert StringOperations().reverse("test") == "tset"


@pytest.mark.regression
def test_regression_string():
    assert StringOperations().count_vowels("AEIOU") == 5


@pytest.mark.xfail
def test_expected_failure():
    assert StringOperations().is_palindrome("not a palindrome")
