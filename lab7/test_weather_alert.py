
from hypothesis import given, strategies as st
from weather_alert import parse_reading, wind_category, rainfall_spread


# 1. parse_reading: Fuzz testing
@given(st.text() | st.none())
def test_parse_reading_no_crash(s):
    result = parse_reading(s)
    assert result is None or (
        isinstance(result, tuple) and len(result) == 2
    )


@given(
    st.floats(allow_nan=False, allow_infinity=False),
    st.integers(min_value=0, max_value=100)
)
def test_parse_reading_valid(temp, humidity):
    result = parse_reading(f"{temp}/{humidity}")
    assert result == (temp, humidity)


# 2. wind_category: Fuzz testing
@given(st.text() | st.none())
def test_wind_category_no_crash(s):
    result = wind_category(s)
    assert result in ('warning', 'advisory', 'none', None)


@given(st.integers(min_value=0))
def test_wind_category_valid(speed):
    if speed >= 89:
        expected = 'warning'
    elif speed >= 39:
        expected = 'advisory'
    else:
        expected = 'none'

    assert wind_category(str(speed)) == expected


# 3. rainfall_spread: Fuzz testing
@given(st.text() | st.none())
def test_rainfall_spread_no_crash(s):
    result = rainfall_spread(s)
    assert result is None or (
        isinstance(result, float) and result >= 0
    )


@given(
    st.lists(
        st.floats(
            min_value=0,
            max_value=1000000,
            allow_nan=False,
            allow_infinity=False
        ),
        min_size=1
    )
)
def test_rainfall_spread_valid(readings):
    csv_input = ','.join(str(r) for r in readings)
    expected = max(readings) - min(readings)

    assert rainfall_spread(csv_input) == expected
