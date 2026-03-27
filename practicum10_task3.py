def sales(cost: float, holiday_day: bool, bonus_card: bool) -> float:
    """Сalculates the total purchase amount
    Args:
        cost: сost of purchase
        holiday_day: is it holiday or not
        bonus_card: user has special card or not
    Returns: total purchase amount
    """

    discount_just_cost = 0
    discount_just_day = 0
    discount_just_bonus = 0

    if 15000 >= cost > 5000:
        discount_just_cost = 0.03
    elif 20000 >= cost > 15000:
        discount_just_cost = 0.05
    elif 30000 >= cost > 20000:
        discount_just_cost = 0.07
    elif cost > 30000:
        discount_just_cost = 0.1

    if holiday_day:
        discount_just_day = 0.03
    if bonus_card:
        discount_just_bonus = 0.05

    total_discount = discount_just_cost + discount_just_day + discount_just_bonus

    if total_discount > 0.15:
        total_discount = 0.15

    return round(cost * (1 - total_discount), 2)












