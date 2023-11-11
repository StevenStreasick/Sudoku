import pytest
import Cell


def test_default_constructor():
    cell = Cell.Cell()
    assert cell.getCellValue() == 1

def test_creation():
    cell = Cell.Cell(3)
    assert cell.getCellValue() == 3

def test_valid_values():
    for n in range(1, 10):
        cell = Cell.Cell(n)
        assert cell.getCellValue() == n, "Invalid value found for a cell created with value " + n
def test_invalid_lowerbounds():
    with pytest.raises(ValueError):
        cell = Cell.Cell(0)
    with pytest.raises(ValueError):
        cell = Cell.Cell(-1)
    
def test_invalid_lowerbounds_largerange():
    for n in range(0, -1000, -1):
        with pytest.raises(ValueError):
            cell = Cell.Cell(n)

def test_invalid_upperbounds():
    with pytest.raises(ValueError):
        cell = Cell.Cell(10)
    with pytest.raises(ValueError):
        cell = Cell.Cell(11)
def test_invalid_upperbounds_largerange():
    for n in range(10, 1010, 1):
        with pytest.raises(ValueError):
            cell = Cell.Cell(n)