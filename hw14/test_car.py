import random
import pytest


@pytest.mark.smoke
def test_change_model(get_new_car):
    new_car = get_new_car
    expected_model = f"BMW {random.randint(1, 7)}"
    new_car.model = expected_model
    assert new_car.model == expected_model


def test_miles_limit_zero(get_new_car):
    new_car = get_new_car
    expected_result = new_car.miles_limit
    assert expected_result == 0


@pytest.mark.smoke
def test_miles_limit(get_new_car_with_miles_limit):
    new_car = get_new_car_with_miles_limit
    expected_result = new_car.miles_limit
    assert expected_result >= 0


@pytest.mark.smoke
def test_start_engine(get_new_car):
    new_car = get_new_car
    expected_result = "Engine started."
    real_result = new_car.start_engine()
    assert real_result == expected_result


@pytest.mark.smoke
def test_drive(get_new_car_with_miles_limit):
    new_car = get_new_car_with_miles_limit
    new_car.start_engine()
    miles_to_drive = random.randint(1, 300)
    exc_driving = f"Driving {miles_to_drive} miles."
    result_of_driving = new_car.drive(miles_to_drive)
    assert result_of_driving == exc_driving


@pytest.mark.smoke
def test_engine_running(get_new_car_with_miles_limit):
    new_car = get_new_car_with_miles_limit
    new_car.start_engine()
    exc_engine_running = "Engine is already running."
    result_engine_running = new_car.start_engine()
    assert exc_engine_running == result_engine_running


@pytest.mark.smoke
def test_engine_stop(get_new_car_with_miles_limit):
    new_car = get_new_car_with_miles_limit
    new_car.start_engine()
    exc_engine_stop = "Engine stopped."
    result_engine_stop = new_car.stop_engine()
    assert exc_engine_stop == result_engine_stop


@pytest.mark.smoke
def test_engine_already_off(get_new_car_with_miles_limit):
    new_car = get_new_car_with_miles_limit
    exc_engine_already_off = "Engine is already off."
    result_already_off = new_car.stop_engine()
    assert exc_engine_already_off == result_already_off


@pytest.mark.smoke
def test_engine_cannot_drive(get_new_car_with_miles_limit):
    new_car = get_new_car_with_miles_limit
    miles_to_drive = random.randint(1, 500)
    drive_the_car = new_car.drive(miles_to_drive)
    exc_engine_cannot_drive = "Cannot drive. Engine is off."
    result_engine_cannot_drive = drive_the_car
    assert exc_engine_cannot_drive == result_engine_cannot_drive


@pytest.mark.smoke
def test_mile_limit_exceeded(get_new_car_with_miles_limit):
    new_car = get_new_car_with_miles_limit
    miles_to_drive = random.randint(301, 1000)
    new_car.start_engine()
    exc_mile_limit_exceeded = f"The miles limit has been exceeded"
    result_mile_limit_exceeded = new_car.drive(miles_to_drive)
    assert exc_mile_limit_exceeded == result_mile_limit_exceeded
