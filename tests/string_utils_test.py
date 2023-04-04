"""
This file includes all the Unit Tests for the custom string methods.
"""

from src.string_utils import StringUtils


def test_join_strings_with_hyphen():
    assert StringUtils.join_strings_with_hyphen("hello", "world") == "hello-world"
