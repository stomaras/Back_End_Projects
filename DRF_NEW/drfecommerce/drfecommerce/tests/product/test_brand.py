import pytest

pytestmark = pytest.mark.django_db


class TestBrandModel:
    def test_str_method(self, brand_factory):
        # Arrange
        x = brand_factory(name="test_brand")
        # Act
        # Assert
        assert x.__str__() == "test_brand"

    
# class TestBrandModel:
#         def test_str_method(self, brand_factory):
#         # Arrange
#         obj = brand_factory(name="test_brand")
#         # Act
#         result = obj.__str__()

#         # Assert
#         assert obj.__str__() == "test_brand"
