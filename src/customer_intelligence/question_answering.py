
import pandas as pd

from customer_intelligence.customer_analytics import (
    calculate_churn_summary,
    get_customer_status,
)



def answer_question(
    question: str,
    customers: pd.DataFrame,
) -> str:
    """Answer supported customer questions using trusted analytics."""
    if not question.strip():
        raise ValueError("Question cannot be empty.")

    normalized_question = question.lower().strip().rstrip("?!.")

    summary = calculate_churn_summary(customers)


    import re

    customer_match = re.search(
        r"\bC\d+\b",
        question,
        re.IGNORECASE,
    )

    if customer_match and any(
        word in normalized_question
        for word in ("customer", "status", "churned", "retained")
    ):
        customer_id = customer_match.group().upper()
        
        try:
            customer = get_customer_status(customers, customer_id)
        except ValueError as error:
            if "was not found" in str(error):
                return f"Customer {customer_id} was not found."
            raise


        return (
            f"Customer {customer['customer_id']} is "
            f"{customer['status'].lower()}."
        )


    if "churn rate" in normalized_question:
        return (
            f"The customer churn rate is "
            f"{summary['churn_rate']:.1%} "
            f"({summary['churned_customers']} out of "
            f"{summary['total_customers']} customers)."
        )

    if "churned" in normalized_question:
        return (
            f"{summary['churned_customers']} out of "
            f"{summary['total_customers']} customers churned."
        )

    if "retained" in normalized_question:
        return (
            f"{summary['retained_customers']} out of "
            f"{summary['total_customers']} customers were retained."
        )

    if "how many customers" in normalized_question or (
        "total customers" in normalized_question
    ):
        return f"There are {summary['total_customers']} customers."

    return (
        "I can't answer that question yet. "
        "Try asking about churn rate, churned customers, "
        "retained customers, or total customers."
    )
