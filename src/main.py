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


print(calculate_taxes([0.5, 1.5, 5.5, 10.5], 100))
print(calculate_taxes([0.5, 1.5, 5.5, 10.5], 10))
print(calculate_taxes([0.5, 1.5, 5.5, 10.5], 1))
