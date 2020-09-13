from src.roman_parser import RomanParser

def test_do_noting():
    # Arrange
    # Act
    # Assert
    assert True

def test_when_number1_get_I():
    romanParser = RomanParser()
    result = romanParser.parse(1)
    assert result == 'I'

def test_when_number2_get_II():
    romanParser = RomanParser()
    result = romanParser.parse(2)
    assert result == 'II'
    
