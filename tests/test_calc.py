import pytest
import numpy as np
import pyangle.calc

def test_square():
    '''Test for the example function'''

    # Arrange
    test_variable_1 = 1
    test_variable_2 = 1
    expected_output_1 = 1
    expected_output_2 = 1

    # Act
    output_1, output_2 = pyangle.calc.square(test_variable_1, test_variable_2)

    # Assert
    assert output_1 == expected_output_1
    assert output_2 == expected_output_2

def test_hypot():
    
    # Arrange
    test_a = 1
    test_b = 1
    test_c = 1.414
    
    # Act
    
    hypot_output = pyangle.calc.hypot(test_a, test_b)
    
    # Assert
    
    assert test_c == pytest.approx(hypot_output, abs=1e-3)
    
def test_pythag():
    
    # Arrange
    test_a = 2
    test_b = 3
    test_c = 3.6056
    
    # Act
    pythag_output = pyangle.calc.pythag(test_a,test_b)
    
    # Assert
    
    assert test_c == pytest.approx(pythag_output, abs=1e3)