def monetary_equivalent_card() -> int:
    """Сalculates the monetary equivalent of the card,
    taking into account bonuses
    """
    cost_of_card = input('Введите, пожалуйста, стоимость карты в долларах:')
    try:
        cost_of_card = int(cost_of_card)
    except ValueError:
        print('Недопустимое значение карты')
        exit()

    if cost_of_card in [5, 10, 25, 50, 100]:
        if cost_of_card == 5 or cost_of_card == 10:
            cost_of_card += 0
        elif cost_of_card == 25:
            cost_of_card += 3
        elif cost_of_card == 50:
            cost_of_card += 8
        elif cost_of_card == 100:
            cost_of_card += 20
    else:
        print('Недопустимое значение карты')
        cost_of_card = 0

    return cost_of_card



print(monetary_equivalent_card())












