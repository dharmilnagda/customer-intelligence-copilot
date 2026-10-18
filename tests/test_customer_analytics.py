
import pandas as pd
import pytest

from customer_intelligence.customer_analytics import (
    calculate_churn_summary,
)


def test_calculates_churn_summary():
    customers = pd.DataFrame({"churn": [0, 1, 0, 1, 0]})

    result = calculate_churn_summary(customers)

    assert result["total_customers"] == 5
    assert result["churned_customers"] == 2
    assert result["retained_customers"] == 3
    assert result["churn_rate"] == 0.4


def test_rejects_empty_customer_data():
    customers = pd.DataFrame({"churn": []})

    with pytest.raises(ValueError, match="cannot be empty"):
        calculate_churn_summary(customers)


def test_rejects_missing_churn_column():
    customers = pd.DataFrame({"customer_id": [1, 2]})

    with pytest.raises(ValueError, match="must contain a 'churn' column"):
        calculate_churn_summary(customers)


def test_rejects_invalid_churn_values():
    customers = pd.DataFrame({"churn": [0, 2]})

    with pytest.raises(ValueError, match="only 0 and 1"):
        calculate_churn_summary(customers)


def test_rejects_missing_churn_values():
    customers = pd.DataFrame({"churn": [0, None]})

    with pytest.raises(ValueError, match="missing values"):
        calculate_churn_summary(customers)

