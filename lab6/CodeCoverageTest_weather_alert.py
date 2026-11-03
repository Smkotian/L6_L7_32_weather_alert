import pytest
from weather_alert import wind_alert, rain_alert, heat_alert, overall_alert


# WIND ALERT TESTS
def test_wind_warning():
    assert wind_alert(89) == "warning"
    assert wind_alert(100) == "warning"


def test_wind_watch():
    assert wind_alert(62) == "watch"
    assert wind_alert(70) == "watch"


def test_wind_advisory():
    assert wind_alert(39) == "advisory"
    assert wind_alert(40) == "advisory"


def test_wind_none():
    assert wind_alert(10) == "none"


# RAIN ALERT TESTS
def test_heavy_rain_saturated():
    assert rain_alert(50, True) == "warning"


def test_heavy_rain_not_saturated():
    assert rain_alert(60, False) == "watch"


def test_moderate_rain_saturated():
    assert rain_alert(10, True) == "watch"


def test_moderate_rain_not_saturated():
    assert rain_alert(20, False) == "advisory"


def test_no_rain_alert():
    assert rain_alert(5, False) == "none"


# HEAT ALERT TESTS
def test_heat_warning():
    assert heat_alert(45, 40) == "warning"


def test_heat_watch():
    assert heat_alert(40, 40) == "watch"


def test_heat_advisory():
    assert heat_alert(35, 40) == "advisory"


def test_heat_none():
    assert heat_alert(25, 40) == "none"


def test_humidity_adjustment():
    assert heat_alert(44, 60) == "warning"


# OVERALL ALERT TESTS
def test_overall_warning():
    assert overall_alert(["advisory", "warning", "watch"]) == "warning"


def test_overall_watch():
    assert overall_alert(["advisory", "watch"]) == "watch"


def test_overall_advisory():
    assert overall_alert(["advisory", "none"]) == "advisory"


def test_overall_none():
    assert overall_alert(["none"]) == "none"


def test_invalid_alert():
    with pytest.raises(ValueError, match="unknown alert"):
        overall_alert(["invalid"])