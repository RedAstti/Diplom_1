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

    def test_get_name(self):
        """Тест получения названия булочки"""
        bun = Bun("test bun", 150)
        assert bun.get_name() == "test bun"

    def test_get_price(self):
        """Тест получения цены булочки"""
        bun = Bun("test bun", 150)
        assert bun.get_price() == 150

    @pytest.mark.parametrize(
        "name,price",
        [
            ("краторная булка N-200i", 1255),
            ("Флюоресцентная булка R2-D3", 988),
        ]
    )
    def test_bun_get_methods(self, name, price):
        """Тест методов get_name и get_price с параметризацией"""
        bun = Bun(name, price)
        assert bun.get_name() == name
        assert bun.get_price() == price
