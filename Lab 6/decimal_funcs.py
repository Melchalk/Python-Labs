from decimal import Decimal, ROUND_FLOOR

def round_average_salary(salary):
    return salary.quantize(Decimal("1.00"), ROUND_FLOOR)

def compare_salary(first, second):
    return Decimal(first).compare(second)