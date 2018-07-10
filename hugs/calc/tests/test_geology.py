"""Test the `geology` module."""

from hugs.calc import snell_angle

from numpy.testing import assert_almost_equal
import pytest

def test_snell():
    """Test the basic wind component calculation."""
    res = snell_angle(12, 2500, 4000)
    assert_almost_equal(res, 19.43022, 4)

def test_snell_top_layer():
    """Test that value error is raised when top layer velocity is 0"""
    with pytest.raises(ValueError):
        res = snell_angle(12,0,4000)
