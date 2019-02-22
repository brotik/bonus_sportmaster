def calculate_bonuses(accumulated, spent):
    """
    >>> calculate_bonuses(15000, 1000)
    50
    >>> calculate_bonuses(150000, 1000)
    70
    >>> calculate_bonuses(200000, 1000)
    100
    >>> calculate_bonuses(100, 20)
    0
    >>> calculate_bonuses(15001, 3000)
    210



    :param accumulated:
    :param spent:
    :return:
    """

    bonus_cost = 1000

    if spent < bonus_cost:
        return 0
    if 1 <= accumulated <= 15_000:
        bonus = 50
    if 15_000 < accumulated <= 150_000:
        bonus = 70
    if accumulated > 150_000:
        bonus = 100

    result = spent // bonus_cost * bonus
    return result

