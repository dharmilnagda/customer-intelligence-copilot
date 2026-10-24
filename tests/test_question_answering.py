
import pandas as pd
import pytest

from customer_intelligence.question_answering import answer_question


@pytest.fixture
def customers():
    return pd.DataFrame({"churn": [0, 1, 0, 1, 0, 0, 1, 0, 0, 1]})


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
