import pytest
from weather_alert import wind_alert, rain_alert, heat_alert, overall_alert


# WIND ALERT: Test True and False outcomes of every condition

def test_wind_branches():
    assert wind_alert(90) == "warning"    # >= 89: True
    assert wind_alert(70) == "watch"      # >= 89: False, >= 62: True
    assert wind_alert(40) == "advisory"   # >= 89: False, >= 62: False, >= 39: True
    assert wind_alert(20) == "none"       # All conditions False


# RAIN ALERT: Test nested conditions

def test_rain_branches():
    assert rain_alert(60, True) == "warning"
    assert rain_alert(60, False) == "watch"

    assert rain_alert(20, True) == "watch"
    assert rain_alert(20, False) == "advisory"

    assert rain_alert(5, True) == "none"


# HEAT ALERT: Test humidity and all heat thresholds

def test_heat_branches():
    assert heat_alert(45, 40) == "warning"
    assert heat_alert(40, 40) == "watch"
    assert heat_alert(35, 40) == "advisory"
    assert heat_alert(25, 40) == "none"

    # Humidity > 40: True, adjustment applied
    assert heat_alert(44, 60) == "warning"


# OVERALL ALERT: Test loop and severity comparisons

def test_overall_empty_list():
    assert overall_alert([]) == "none"


def test_overall_increasing_severity():
    assert overall_alert(["none", "advisory", "watch", "warning"]) == "warning"


def test_overall_decreasing_severity():
    assert overall_alert(["warning", "watch", "advisory", "none"]) == "warning"


def test_overall_same_severity():
    assert overall_alert(["watch", "watch"]) == "watch"


def test_overall_invalid_alert():
    with pytest.raises(ValueError, match="unknown alert"):
        overall_alert(["invalid"])