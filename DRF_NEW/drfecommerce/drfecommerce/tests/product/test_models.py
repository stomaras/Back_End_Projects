import pytest

pytestmark = pytest.mark.django_db


class TestCategoryModel:
    def test_str_method(self, category_factory):
        # Arrange
        x = category_factory(name="test_cat")
        # Act
        # Assert
        assert x.__str__() == "test_cat"

    
# class TestBrandModel:
#         def test_str_method(self, brand_factory):
#         # Arrange
#         obj = brand_factory(name="test_brand")
#         # Act
#         result = obj.__str__()

#         # Assert
#         assert obj.__str__() == "test_brand"
