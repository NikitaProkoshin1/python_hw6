from typing import Dict, List
from turtle import update

__all__ = ['calculate_portfolio_value',
           'calculate_portfolio_return',
           'get_most_profitable_stock']

_start_prices: Dict[str, float] = {}


def calculate_portfolio_value(stocks: Dict[str, int],
                              prices: Dict[str, float]) -> float:
    total_prices: float = 0.0

    global _start_prices
    _start_prices.update(prices)

    for company_name in stocks.keys():
        total_prices += \
            stocks[company_name] * prices[company_name]
    return total_prices


def calculate_portfolio_return(initial_value: float,
                               current_value: float) -> float:
    return ((current_value * 100) / initial_value) - 100


def get_most_profitable_stock(stocks: Dict[str, int],
                              prices_now: Dict[str, float]) -> str:
    difference: Dict[str, float] = {}

    for company_name in stocks.keys():
        difference[company_name] = \
            prices_now[company_name]- _start_prices[company_name]

    found_values: List[str] = [max(difference, key=difference.get)]

    for company_name in stocks.keys():
        if (difference[found_values[0]] == difference[company_name]) \
                and (company_name not in found_values):
            found_values.append(company_name)

    return ', '.join(found_values)

if __name__ == "__main__":
    stocks_for_calculate_portfolio_value = \
        {"AAPL": 10, "GOOGL": 5, "MSFT": 8, "NN": 1}
    stocks_for_get_most_profitable_stock = \
        {"GOOGL": 5, "MSFT": 8, "NN": 1}
    prices_start = \
        {"AAPL": 180.89, "GOOGL": 580.67, "MSFT": 880.45, "NN": 1600.23}
    prices_stop = \
        {"GOOGL": 590.67, "MSFT": 900.45, "NN": 1590.23}
    initial_value: float = 10000.00
    current_value: float = 15000.00

    print(calculate_portfolio_value(stocks=
                                    stocks_for_calculate_portfolio_value,
                                    prices=
                                    prices_start))

    print(calculate_portfolio_return(initial_value=
                                     initial_value,
                                     current_value=
                                     current_value))
    print(get_most_profitable_stock(stocks=
                                    stocks_for_get_most_profitable_stock,
                                    prices_now=
                                    prices_stop))
