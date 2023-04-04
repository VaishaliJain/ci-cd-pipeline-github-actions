"""
This file includes all the Unit Tests for the custom numerical methods.
"""
import pytest

from src.number_utils import NumberUtils


def test_validate_number_in_range():
    assert NumberUtils.validate_number_in_range(70, 10, 100) is None

    with pytest.raises(ValueError):
        NumberUtils.validate_number_in_range(70, 90, 100)
