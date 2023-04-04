"""
This file includes a few numerical operations.
"""


class NumberUtils:
    """
    Implements a few numerical operations.
    """

    @staticmethod
    def validate_number_in_range(num, range_start, range_end) -> None:
        """
        Validates if a number is in given range
        :param num: Number to be validated
        :param range_start: Start of the range
        :param range_end: End if the range
        Raises:
            ValueError: If the given number isn't in the provided range
        """
        if not (range_start <= num <= range_end):
            message = f"ERROR: num must be between `{range_start}` and `{range_end}`, but we have num as `{num}`."
            raise ValueError(message)
