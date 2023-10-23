import pytest
from hw14.car import Car


@pytest.fixture()
def get_new_car():
    new_car = Car("BMW", "x5", )
    return new_car


@pytest.fixture()
def get_new_car_with_miles_limit():
    new_car = Car("Audi", "a5", 300)
    return new_car
