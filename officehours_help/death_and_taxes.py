# Cade Crandall


def income_tax(is_single, income):
    """
    Returns a floating point for estimated income tax
    :param is_single: boolean that describes filing status
    :param income: total income in USD
    :type is_single: bool
    :type income: int
    :return: estimated income tax
    :rtype: float
    """
    if is_single:
        bracket = {
            9325: 0.1,
            37950: 0.15,
            91900: 0.25,
            191650: 0.28,
            416900: 0.33,
            418400: 0.35,
            float('inf'): 0.396
        }
    else:
        bracket = {
            18650: 0.1,
            75900: 0.15,
            153100: 0.25,
            233350: 0.28,
            416900: 0.33,
            470700: 0.35,
            float('inf'): 0.396
        }

    tax = 0
    untaxed_income = income
    lower_bound = 0
    for upper_bound, percent in bracket.items():
        if income >= upper_bound:
            # While the total income is greater than the current bracket
            # add to the income tax bracket_percent * bracket_range
            tax += (percent * (upper_bound - lower_bound))
            untaxed_income = income - upper_bound
            # Untaxed income is the income - current
            lower_bound = upper_bound
            # Update upper bound for next calculation
        else:
            # Once the highest income bracket is reached,
            # add to the tax the remainder of untaxed_income * bracket_percent
            tax += (untaxed_income * percent)
            break
    return int(tax)


tax = income_tax(True, 50000)
print(tax)
