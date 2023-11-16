from src.interest_calculator import calculate_interest, define_interest_rate


def test_return_different_interest_rates_based_on_account_type(mocker):
    mocker.patch(
        "src.interest_calculator.define_interest_rate",
        side_effect=lambda account_type: {
            "saving": 0.02,
            "current": 0.01,
        }.get(account_type, 0.005),
    )

    result_saving = calculate_interest("saving", 1000)
    result_current = calculate_interest("current", 1000)
    result_default = calculate_interest("default", 1000)

    assert result_saving == 20.0
    assert result_current == 10.0
    assert result_default == 5.0
