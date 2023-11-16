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
