import pytest
from math_operations import add, sub


class TestMathOperations:
    """Test class for math operations module."""
    
    def test_add_positive_numbers(self):
        """Test adding positive numbers."""
        assert add(2, 3) == 5
        assert add(10, 15) == 25
        assert add(1, 1) == 2
    
    def test_add_negative_numbers(self):
        """Test adding negative numbers."""
        assert add(-2, -3) == -5
        assert add(-10, -5) == -15
        assert add(-1, -1) == -2
    
    def test_add_mixed_numbers(self):
        """Test adding positive and negative numbers."""
        assert add(5, -3) == 2
        assert add(-5, 3) == -2
        assert add(10, -10) == 0
    
    def test_add_zero(self):
        """Test adding zero."""
        assert add(0, 5) == 5
        assert add(5, 0) == 5
        assert add(0, 0) == 0
    
    def test_add_floats(self):
        """Test adding floating point numbers."""
        assert add(2.5, 3.5) == 6.0
        assert add(1.1, 2.2) == pytest.approx(3.3)
        assert add(-1.5, 1.5) == 0.0
    
    def test_sub_positive_numbers(self):
        """Test subtracting positive numbers."""
        assert sub(5, 3) == 2
        assert sub(10, 4) == 6
        assert sub(1, 1) == 0
    
    def test_sub_negative_numbers(self):
        """Test subtracting negative numbers."""
        assert sub(-2, -3) == 1
        assert sub(-10, -5) == -5
        assert sub(-1, -1) == 0
    
    def test_sub_mixed_numbers(self):
        """Test subtracting positive and negative numbers."""
        assert sub(5, -3) == 8
        assert sub(-5, 3) == -8
        assert sub(10, -10) == 20
    
    def test_sub_zero(self):
        """Test subtracting zero."""
        assert sub(5, 0) == 5
        assert sub(0, 5) == -5
        assert sub(0, 0) == 0
    
    def test_sub_floats(self):
        """Test subtracting floating point numbers."""
        assert sub(5.5, 2.5) == 3.0
        assert sub(3.3, 1.1) == pytest.approx(2.2)
        assert sub(1.5, 1.5) == 0.0


# Edge case tests
class TestEdgeCases:
    """Test edge cases for math operations."""
    
    def test_large_numbers(self):
        """Test with large numbers."""
        large_num = 999999999
        assert add(large_num, 1) == 1000000000
        assert sub(large_num, 1) == 999999998
    
    def test_very_small_numbers(self):
        """Test with very small decimal numbers."""
        small_num = 0.0000001
        assert add(small_num, small_num) == pytest.approx(0.0000002)
        assert sub(small_num, small_num) == pytest.approx(0.0)


# Parametrized tests for comprehensive coverage
@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300),
    (1.5, 2.5, 4.0),
])
def test_add_parametrized(a, b, expected):
    """Parametrized test for add function."""
    assert add(a, b) == expected


@pytest.mark.parametrize("a,b,expected", [
    (5, 3, 2),
    (0, 0, 0),
    (1, -1, 2),
    (200, 100, 100),
    (5.5, 2.5, 3.0),
])
def test_sub_parametrized(a, b, expected):
    """Parametrized test for sub function."""
    assert sub(a, b) == expected
