from typing import Iterator
from unittest.mock import MagicMock, patch

import pytest

from app import main


@pytest.fixture()
def mocked_get_exchange_rate_prediction() -> Iterator[MagicMock]:
    with patch("app.main.get_exchange_rate_prediction") as mock_test:
        yield mock_test


def test_buy_more_when_prediction_more_than_5_percent_higher(
    mocked_get_exchange_rate_prediction: MagicMock,
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 4

    assert main.cryptocurrency_action(2) == "Buy more cryptocurrency"


def test_sell_all_when_prediction_more_than_5_percent_lower(
    mocked_get_exchange_rate_prediction: MagicMock,
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1

    assert main.cryptocurrency_action(2) == "Sell all your cryptocurrency"


def test_do_nothing_when_prediction_exactly_5_percent_higher(
    mocked_get_exchange_rate_prediction: MagicMock,
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 100

    assert main.cryptocurrency_action(105) == "Do nothing"
