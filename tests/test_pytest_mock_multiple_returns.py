
import pytest

class TestMagicMock:
    def test_mock_with_side_effect(self, mocker):
        m = mocker.MagicMock()
        m.side_effect = lambda *x: {
            (10, 10): 20,
            (20, 20): 40,
            (30, 30): 60
        }[x]

        result1 = m(30, 30)
        assert result1 == 60

        result2 = m(20, 20)
        assert result2 == 40
