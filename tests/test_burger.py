import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    """Тесты для класса Burger"""

    def test_burger_initialization(self):
        """Тест инициализации бургера"""
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = 120
        mock_bun.get_name.return_value = "basic bun"

        burger.set_buns(mock_bun)

        assert burger.get_price() == 240

        receipt_lines = burger.get_receipt().split('\n')
        assert receipt_lines == [
            "(==== basic bun ====)",
            "(==== basic bun ====)",
            "",
            "Price: 240",
        ]
        mock_bun.get_price.assert_called()
        mock_bun.get_name.assert_called()

    def test_set_buns(self):
        """Тест установки булочки"""
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self):
        """Тест добавления ингредиента"""
        burger = Burger()
        mock_ingredient = Mock(spec=Ingredient)
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    def test_add_multiple_ingredients(self):
        """Тест добавления нескольких ингредиентов"""
        burger = Burger()
        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient2 = Mock(spec=Ingredient)
        mock_ingredient3 = Mock(spec=Ingredient)
        
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.add_ingredient(mock_ingredient3)
        
        assert len(burger.ingredients) == 3
        assert burger.ingredients[0] == mock_ingredient1
        assert burger.ingredients[1] == mock_ingredient2
        assert burger.ingredients[2] == mock_ingredient3

    @pytest.mark.parametrize("index", [0, 1, 2])
    def test_remove_ingredient(self, index):
        """Тест удаления ингредиента по индексу"""
        burger = Burger()
        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient2 = Mock(spec=Ingredient)
        mock_ingredient3 = Mock(spec=Ingredient)
        
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.add_ingredient(mock_ingredient3)
        
        initial_count = len(burger.ingredients)
        burger.remove_ingredient(index)
        
        assert len(burger.ingredients) == initial_count - 1

    def test_remove_first_ingredient(self):
        """Тест удаления первого ингредиента"""
        burger = Burger()
        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient2 = Mock(spec=Ingredient)
        
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.remove_ingredient(0)
        
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient2

    def test_remove_last_ingredient(self):
        """Тест удаления последнего ингредиента"""
        burger = Burger()
        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient2 = Mock(spec=Ingredient)
        
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.remove_ingredient(1)
        
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient1

    @pytest.mark.parametrize(
        "old_index,new_index",
        [
            (0, 1),
        ]
    )
    def test_move_ingredient(self, old_index, new_index):
        """Тест перемещения ингредиента с параметризацией"""
        burger = Burger()
        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient2 = Mock(spec=Ingredient)
        mock_ingredient3 = Mock(spec=Ingredient)
        
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.add_ingredient(mock_ingredient3)
        
        ingredient_to_move = burger.ingredients[old_index]
        burger.move_ingredient(old_index, new_index)
        
        assert burger.ingredients[new_index] == ingredient_to_move
        assert len(burger.ingredients) == 3

    def test_get_price_with_bun_only(self):
        """Тест расчёта цены бургера только с булочкой"""
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = 100
        
        burger.set_buns(mock_bun)
        price = burger.get_price()
        
        assert price == 200  # булочка используется дважды (верх и низ)
        mock_bun.get_price.assert_called()

    def test_get_price_with_bun_and_ingredients(self):
        """Тест расчёта цены бургера с булочкой и ингредиентами"""
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = 100
        
        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient1.get_price.return_value = 50
        
        mock_ingredient2 = Mock(spec=Ingredient)
        mock_ingredient2.get_price.return_value = 75
        
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        
        price = burger.get_price()
        
        assert price == 325  # 100*2 + 50 + 75
        mock_bun.get_price.assert_called()
        mock_ingredient1.get_price.assert_called()
        mock_ingredient2.get_price.assert_called()

    @pytest.mark.parametrize(
        "bun_price,ingredient_prices,expected_price",
        [
            (100, [50, 75], 325),
            (200, [100, 150, 200], 850),
            (150, [], 300),
            (50, [25], 125),
        ]
    )
    def test_get_price_parametrized(self, bun_price, ingredient_prices, expected_price):
        """Тест расчёта цены с параметризацией"""
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)
        
        for ingredient_price in ingredient_prices:
            mock_ingredient = Mock(spec=Ingredient)
            mock_ingredient.get_price.return_value = ingredient_price
            burger.add_ingredient(mock_ingredient)
        
        price = burger.get_price()
        assert price == expected_price

    def test_get_receipt_with_bun_only(self):
        """Тест получения чека с одной булочкой"""
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100
        
        burger.set_buns(mock_bun)
        receipt = burger.get_receipt()
        
        assert "(==== black bun ====)" in receipt
        assert "Price: 200" in receipt
        mock_bun.get_name.assert_called()

    def test_get_receipt_with_ingredients(self):
        """Тест получения чека с ингредиентами"""
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "white bun"
        mock_bun.get_price.return_value = 150
        
        mock_sauce = Mock(spec=Ingredient)
        mock_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_sauce.get_name.return_value = "hot sauce"
        mock_sauce.get_price.return_value = 50
        
        mock_filling = Mock(spec=Ingredient)
        mock_filling.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_filling.get_name.return_value = "cutlet"
        mock_filling.get_price.return_value = 100
        
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        
        receipt = burger.get_receipt()
        
        assert "(==== white bun ====)" in receipt
        assert "= sauce hot sauce =" in receipt
        assert "= filling cutlet =" in receipt
        assert "Price: 450" in receipt  # 150*2 + 50 + 100 = 450

    def test_get_receipt_format(self):
        """Тест формата чека"""
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "test bun"
        mock_bun.get_price.return_value = 100
        
        burger.set_buns(mock_bun)
        receipt = burger.get_receipt()
        
        lines = receipt.split('\n')
        assert lines[0] == "(==== test bun ====)"
        assert lines[-3] == "(==== test bun ====)"  # Перед пустой строкой
        assert lines[-2] == ""  # Пустая строка
        assert lines[-1].startswith("Price: ")

    def test_get_receipt_ingredient_order(self):
        """Тест порядка ингредиентов в чеке"""
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "bun"
        mock_bun.get_price.return_value = 100
        
        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient1.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient1.get_name.return_value = "sauce1"
        mock_ingredient1.get_price.return_value = 50
        
        mock_ingredient2 = Mock(spec=Ingredient)
        mock_ingredient2.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_ingredient2.get_name.return_value = "filling1"
        mock_ingredient2.get_price.return_value = 75
        
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        
        receipt = burger.get_receipt()
        lines = receipt.split('\n')
        
        # Проверяем что ингредиенты идут в правильном порядке
        sauce_index = next(i for i, line in enumerate(lines) if "sauce1" in line)
        filling_index = next(i for i, line in enumerate(lines) if "filling1" in line)
        assert sauce_index < filling_index
