"""
This file includes a few string operations.
"""


class StringUtils:
    """
    Implements a few string operations.
    """

    @staticmethod
    def join_strings_with_hyphen(a, b):
        """
      Custom join two strings with "-" in between
      :param a: First string
      :param b: Second string
      :return: Result of custom string join
      """
        return a + "-" + b
