
from customer_intelligence.customer_insights import summarize_churn


def test_summarizes_churn_in_business_language():
    summary = {
        "total_customers": 10,
        "churned_customers": 4,
        "retained_customers": 6,
        "churn_rate": 0.4,
    }

    result = summarize_churn(summary)

    assert result == "4 of 10 customers churned (40.0%)."
