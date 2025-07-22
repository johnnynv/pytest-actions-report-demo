# This is NVIDIA proprietary code and confidential. All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.
#
import pytest
from pytestshow.math_ops import MathOperations


@pytest.mark.fast
@pytest.mark.positive
class TestMathBasicOperations:
    def test_add(self, math_ops):
        assert math_ops.add(2, 3) == 5

    def test_subtract(self, math_ops):
        assert math_ops.subtract(5, 3) == 2

    def test_multiply(self, math_ops):
        assert math_ops.multiply(3, 4) == 12


@pytest.mark.slow
@pytest.mark.positive
class TestMathAdvancedOperations:
    def test_divide(self, math_ops):
        assert math_ops.divide(10, 2) == 5

    def test_factorial(self, math_ops):
        assert math_ops.factorial(5) == 120


@pytest.mark.negative
class TestMathNegativeCases:
    def test_divide_by_zero(self, math_ops):
        with pytest.raises(ValueError):
            math_ops.divide(5, 0)

    def test_negative_factorial(self, math_ops):
        with pytest.raises(ValueError):
            math_ops.factorial(-1)


@pytest.mark.smoke
def test_smoke_math():
    assert MathOperations().add(1, 1) == 2


@pytest.mark.regression
def test_regression_math():
    assert MathOperations().multiply(2, 3) == 6


@pytest.mark.skip(reason="Not implemented yet")
def test_future_feature():
    assert False
