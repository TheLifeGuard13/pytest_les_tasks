def calculate_taxes(prices: list[float], tax_rate: float) -> list[float]:
    """Функция вычисляет стоимость товаров с учётом налога."""

    if tax_rate < 0:
        raise ValueError('Неверный налоговый процент')

    taxed_prices = []

    for price in prices:
        if price <= 0:
            raise ValueError('Неверная цена')
        tax = price * tax_rate / 100
        taxed_prices.append(price + tax)

    return taxed_prices


def calculate_tax(price: float, tax_rate: float) -> float:
    """Функция вычисляет стоимость товара с учётом налога."""
    if price <= 0:
        raise ValueError('Неверная цена')
    elif tax_rate < 0 or tax_rate >= 100:
        raise ValueError('Неверный налоговый процент')
    else:
        taxed_price = price * tax_rate / 100

    return taxed_price
