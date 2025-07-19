import pytest


@pytest.fixture
def math_ops():
    from pytestshow.math_ops import MathOperations

    return MathOperations()


@pytest.fixture
def string_ops():
    from pytestshow.string_ops import StringOperations

    return StringOperations()


@pytest.fixture(params=[1, 2, 3])
def sample_numbers(request):
    return request.param
