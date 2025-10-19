"""Dice Evaluator module."""


class DiceEvaluator():  # noqa: H601
    """Evaluates dice."""

    @staticmethod
    def rolled_one(value_one, value_two):
        """Determine if player may continue or not.

        :param value_one: Value of first die.
        :type value_one: :py:obj:`int`
        :param value_two: Value of second die.
        :type value_two: :py:obj:`int`
        :return: True if one of the two dice rolled atleast a single one, else false
        :return type: :py:obj:`True` | :py:obj:`False`
        """
        if value_one == 1 or value_two == 1:
            return True
        return False

    @staticmethod
    def rolled_two_ones(value_one, value_two):
        """Determine if player rolled two ones.

        :param value_one: Value of first die.
        :type value_one: :py:obj:`int`
        :param value_two: Value of second die.
        :type value_two: :py:obj:`int`
        :return: True if two ones were rolled, else false
        :return type: :py:obj:`True` | :py:obj:`False`
        """
        if value_one == 1 and value_two == 1:
            return True
        return False
