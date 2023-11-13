import pytest
from interest_calculator import calculate_interest, calculate_interest_rate

def test_return_different_interest_rates_based_on_account_type(mocker):
    def interest_rate_side_effect(account_type):
        if account_type == 'saving':
            return 0.02
        elif account_type == 'current':
            return 0.01
        else:
            return 0.005

    mock_interest_rate = mocker.patch('interest_calculator.calculate_interest_rate', side_effect=interest_rate_side_effect)

    result_saving = calculate_interest('saving', 1000)
    result_current = calculate_interest('current', 1000)
    result_default = calculate_interest('default', 1000)

    assert result_saving == 20.0
    assert result_current == 10.0
    assert result_default == 5.0
