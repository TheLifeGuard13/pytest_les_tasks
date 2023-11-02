from src.main import calculate_taxes

import pytest


def test_wrong_rate():
    with pytest.raises(ValueError):
        calculate_taxes([0.5, 1.5, 5.5, 10.5], -100)


def test_wrong_price():
    with pytest.raises(ValueError):
        calculate_taxes([-0.5, 1.5, 5.5, 10.5], 100)


@pytest.fixture
def prices():
    return [0.5, 1.5, 5.5, 10.5]


@pytest.fixture
def rate():
    return 100


def test_get_taxed_price(prices, rate):
    assert calculate_taxes(prices, rate) == [1.0, 3.0, 11.0, 21.0]


@pytest.mark.parametrize('price, tax, expected', [
    ([0.5, 1.5, 5.5, 10.5], 100, [1.0, 3.0, 11.0, 21.0]),
    ([0.5, 1.5, 5.5, 10.5], 10, [0.55, 1.65, 6.05, 11.55]),
    ([0.5, 1.5, 5.5, 10.5], 1, [0.505, 1.515, 5.555, 10.605]),
    # ([0.5, 1.5, 5.5, 10.5], -1, ValueError)
])
def test_get_taxed_price_para(price, tax, expected):
    assert calculate_taxes(price, tax) == expected
