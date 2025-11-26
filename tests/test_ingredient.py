import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    """Тесты для класса Ingredient"""

    @pytest.mark.parametrize(
        "ingredient_type,name,price",
        [
            (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
            (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
            (INGREDIENT_TYPE_FILLING, "cutlet", 100),
            (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        ]
    )
    def test_ingredient_initialization(self, ingredient_type, name, price):
        """Тест инициализации ингредиента с разными параметрами"""
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.type == ingredient_type
        assert ingredient.name == name
        assert ingredient.price == price

    def test_get_price(self):
        """Тест получения цены ингредиента"""
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "test sauce", 150)
        assert ingredient.get_price() == 150

    def test_get_name(self):
        """Тест получения названия ингредиента"""
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "test filling", 250)
        assert ingredient.get_name() == "test filling"

    def test_get_type(self):
        """Тест получения типа ингредиента"""
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "test sauce", 150)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE

    @pytest.mark.parametrize(
        "ingredient_type",
        [
            INGREDIENT_TYPE_SAUCE,
            INGREDIENT_TYPE_FILLING,
        ]
    )
    def test_ingredient_types(self, ingredient_type):
        """Тест создания ингредиентов разных типов"""
        ingredient = Ingredient(ingredient_type, "test", 100)
        assert ingredient.get_type() == ingredient_type
