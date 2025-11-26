import pytest
from praktikum.bun import Bun


class TestBun:
    """Тесты для класса Bun"""

    @pytest.mark.parametrize(
        "name,price",
        [
            ("black bun", 100),
            ("white bun", 200),
            ("red bun", 300),
            ("Флюоресцентная булка R2-D3", 988),
        ]
    )
    def test_bun_initialization(self, name, price):
        """Тест инициализации булочки с разными параметрами"""
        bun = Bun(name, price)
        assert bun.name == name
        assert bun.price == price

    @pytest.mark.parametrize(
        "name,price",
        [
            ("classic bun", 0),
            ("Булочка №42", 999.99),
            ("Bun-π_special_123", 150),
            ("スペース bun!", 75.5),
        ]
    )
    def test_bun_get_methods_equivalence_classes(self, name, price):
        """Тест методов get_name и get_price для разных классов значений"""
        bun = Bun(name, price)
        assert bun.get_name() == name
        assert bun.get_price() == price
