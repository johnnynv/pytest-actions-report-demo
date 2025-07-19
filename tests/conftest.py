import pytest


@pytest.fixture
def math_ops():
    from src.math_ops import MathOperations

    return MathOperations()


@pytest.fixture
def string_ops():
    from src.string_ops import StringOperations

    return StringOperations()


@pytest.fixture(params=[1, 2, 3])
def sample_numbers(request):
    return request.param
