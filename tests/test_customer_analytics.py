
import pandas as pd
import pytest

from customer_intelligence.customer_analytics import (
    calculate_churn_summary,
    get_customer_status,
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


def test_get_customer_status_for_churned_customer():
    customers = pd.DataFrame(
        {
            "customer_id": ["C001", "C002"],
            "churn": [0, 1],
        }
    )

    result = get_customer_status(customers, "C002")

    assert result == {
        "customer_id": "C002",
        "churn": 1,
        "status": "Churned",
    }


def test_get_customer_status_for_retained_customer():
    customers = pd.DataFrame(
        {
            "customer_id": ["C001", "C002"],
            "churn": [0, 1],
        }
    )

    result = get_customer_status(customers, "C001")

    assert result["status"] == "Retained"


def test_get_customer_status_for_unknown_customer():
    customers = pd.DataFrame(
        {
            "customer_id": ["C001"],
            "churn": [0],
        }
    )

    with pytest.raises(ValueError, match="was not found"):
        get_customer_status(customers, "C999")


def test_get_customer_status_rejects_duplicate_ids():
    customers = pd.DataFrame(
        {
            "customer_id": ["C001", "C001"],
            "churn": [0, 1],
        }
    )

    with pytest.raises(ValueError, match="must be unique"):
        get_customer_status(customers, "C001")
