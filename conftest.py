import pytest
from api.testPreparation import TestData

@pytest.fixture
def test_data():
    return TestData()