
import pandas as pd
import pytest

from customer_intelligence.question_answering import answer_question




@pytest.fixture
def customers():
    return pd.DataFrame(
        {
            "customer_id": [
                "C001", "C002", "C003", "C004", "C005",
                "C006", "C007", "C008", "C009", "C010",
            ],
            "churn": [0, 1, 0, 1, 0, 0, 1, 0, 0, 1],
        }
    )



def test_answers_churn_rate_question(customers):
    result = answer_question("What is our churn rate?", customers)

    assert result == (
        "The customer churn rate is 40.0% "
        "(4 out of 10 customers)."
    )


def test_answers_churned_customer_question(customers):
    result = answer_question("How many customers churned?", customers)

    assert result == "4 out of 10 customers churned."


def test_answers_retained_customer_question(customers):
    result = answer_question("How many customers were retained?", customers)

    assert result == "6 out of 10 customers were retained."


def test_handles_unsupported_question(customers):
    result = answer_question("Which marketing campaign performed best?", customers)

    assert "can't answer that question yet" in result


def test_rejects_empty_question(customers):
    with pytest.raises(ValueError, match="Question cannot be empty"):
        answer_question("   ", customers)


def test_answers_customer_status_question(customers):
    result = answer_question(
        "What is the churn status of customer C004?",
        customers,
    )

    assert result == "Customer C004 is churned."


def test_answers_lowercase_customer_id(customers):
    result = answer_question(
        "What is the status of customer c001?",
        customers,
    )

    assert result == "Customer C001 is retained."


def test_handles_unknown_customer(customers):
    result = answer_question(
        "What is the status of customer C999?",
        customers,
    )

    assert result == "Customer C999 was not found."
