"""
This file includes all the Unit Tests for the custom string methods.
"""

from unittest import TestCase
from src.string_utils import StringUtils


class TestScript(TestCase):
    """
    Checks the functionality of the String utils.
    """

    def test_custom_string_tests(self):
        """
        Checks the functionality of the addition.
        """
        assert StringUtils.custom_join_strings("hello", "world") == "hello-world"
