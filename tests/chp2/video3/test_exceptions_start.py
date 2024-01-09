from scripts.chp2.video3.mapmaker_exceptions_start import Point
import pytest


def test_make_one_point():
    p1 = Point("Dakar", 14.7167, 17.4677)
    assert p1.get_lat_long() == (14.7167, 17.4677)


def test_invalid_point_generation():
    with pytest.raises(ValueError) as exp:
        Point("Buenos Ares", 12.11386, -555.0269)
    assert str(exp.value) == "Invalid latitude, longitude combination"


def test_name_is_string():
    with pytest.raises(ValueError) as exp:
        Point(23, 12.1138, 37.3224)
    assert str(exp.value) == "Name must be a string"
