'''Module providing a function.'''
import re
from decimal import Decimal as dec
from typing import Callable

def generator_numbers(text: str):
    '''generator parsing text for real numbers'''
    for match in re.finditer(r'\b\d+\.\d+\b', text):
        yield dec(match.group())

def sum_profit(text: str, func: Callable) -> dec:
    '''function which calls generator'''
    return sum(func(text))

#text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
#total_income = sum_profit(text, generator_numbers)
#print(f"Загальний дохід: {total_income}")
