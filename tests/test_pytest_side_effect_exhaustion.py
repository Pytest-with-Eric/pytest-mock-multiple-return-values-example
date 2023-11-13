import pytest

def test_side_effect_exhaustion(mocker):
    # Create a MagicMock with side_effect as an iterable
    mock_iterable = mocker.MagicMock()
    mock_iterable.side_effect = [1, 2, 3]

    # Consume all elements from the iterable
    assert mock_iterable() == 1
    assert mock_iterable() == 2
    assert mock_iterable() == 3

    # Further calls will raise StopIteration
    with pytest.raises(StopIteration):
        mock_iterable()

def test_side_effect_cyclic(mocker):
    # Create a MagicMock with side_effect as a cyclic iterable
    cyclic_values = [1, 2, 3]
    mock_cyclic = mocker.MagicMock()

    def cyclic_side_effect():
        value = cyclic_values.pop(0)
        cyclic_values.append(value)
        return value

    mock_cyclic.side_effect = cyclic_side_effect

    # Consume all elements from the iterable
    assert mock_cyclic() == 1
    assert mock_cyclic() == 2
    assert mock_cyclic() == 3

    # It will start again from the beginning in a cyclic manner
    assert mock_cyclic() == 1

def test_side_effect_callable(mocker):
    # Create a MagicMock with side_effect as a callable
    mock_callable = mocker.MagicMock()
    
    def callable_side_effect(x):
        result = x * 2
        if result > 20:  # Some condition indicating exhaustion
            raise StopIteration
        return result

    mock_callable.side_effect = callable_side_effect

    # The callable will be invoked with the same argument
    assert mock_callable(5) == 10
    assert mock_callable(8) == 16

    # If the callable raises StopIteration, it signals exhaustion
    with pytest.raises(StopIteration):
        mock_callable(15)
