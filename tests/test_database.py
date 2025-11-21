import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    """Тесты для класса Database"""

    def test_database_initialization(self):
        """Тест инициализации базы данных"""
        database = Database()
        assert isinstance(database.buns, list)
        assert isinstance(database.ingredients, list)
        assert len(database.buns) == 3
        assert len(database.ingredients) == 6

    def test_available_buns_returns_list(self):
        """Тест что available_buns возвращает список"""
        database = Database()
        buns = database.available_buns()
        assert isinstance(buns, list)
        assert len(buns) == 3

    def test_available_buns_contains_bun_objects(self):
        """Тест что available_buns возвращает объекты Bun"""
        database = Database()
        buns = database.available_buns()
        for bun in buns:
            assert isinstance(bun, Bun)

    def test_available_buns_names(self):
        """Тест названий булочек в базе данных"""
        database = Database()
        buns = database.available_buns()
        bun_names = [bun.get_name() for bun in buns]
        assert "black bun" in bun_names
        assert "white bun" in bun_names
        assert "red bun" in bun_names

    def test_available_buns_prices(self):
        """Тест цен булочек в базе данных"""
        database = Database()
        buns = database.available_buns()
        bun_prices = [bun.get_price() for bun in buns]
        assert 100 in bun_prices
        assert 200 in bun_prices
        assert 300 in bun_prices

    def test_available_ingredients_returns_list(self):
        """Тест что available_ingredients возвращает список"""
        database = Database()
        ingredients = database.available_ingredients()
        assert isinstance(ingredients, list)
        assert len(ingredients) == 6

    def test_available_ingredients_contains_ingredient_objects(self):
        """Тест что available_ingredients возвращает объекты Ingredient"""
        database = Database()
        ingredients = database.available_ingredients()
        for ingredient in ingredients:
            assert isinstance(ingredient, Ingredient)

    def test_available_ingredients_has_sauces(self):
        """Тест что в базе есть соусы"""
        database = Database()
        ingredients = database.available_ingredients()
        sauces = [ing for ing in ingredients if ing.get_type() == INGREDIENT_TYPE_SAUCE]
        assert len(sauces) == 3

    def test_available_ingredients_has_fillings(self):
        """Тест что в базе есть начинки"""
        database = Database()
        ingredients = database.available_ingredients()
        fillings = [ing for ing in ingredients if ing.get_type() == INGREDIENT_TYPE_FILLING]
        assert len(fillings) == 3

    def test_available_ingredients_names(self):
        """Тест названий ингредиентов в базе данных"""
        database = Database()
        ingredients = database.available_ingredients()
        ingredient_names = [ing.get_name() for ing in ingredients]
        assert "hot sauce" in ingredient_names
        assert "sour cream" in ingredient_names
        assert "cutlet" in ingredient_names
        assert "dinosaur" in ingredient_names
