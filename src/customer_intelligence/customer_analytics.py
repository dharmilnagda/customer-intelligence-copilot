
import pandas as pd


def calculate_churn_summary(
    customers: pd.DataFrame,
) -> dict[str, int | float]:
    """Calculate basic churn metrics from customer-level data."""
    if "churn" not in customers.columns:
        raise ValueError("Customer data must contain a 'churn' column.")

    if customers.empty:
        raise ValueError("Customer data cannot be empty.")

    if customers["churn"].isna().any():
        raise ValueError("The 'churn' column cannot contain missing values.")

    if not customers["churn"].isin([0, 1]).all():
        raise ValueError("The 'churn' column must contain only 0 and 1.")

    total_customers = len(customers)
    churned_customers = int(customers["churn"].sum())

    return {
        "total_customers": total_customers,
        "churned_customers": churned_customers,
        "retained_customers": total_customers - churned_customers,
        "churn_rate": churned_customers / total_customers,
    }


def summarize_churn(summary: dict[str, int | float]) -> str:
    """Convert churn metrics into a concise business summary."""
    total = summary["total_customers"]
    churned = summary["churned_customers"]
    churn_rate = summary["churn_rate"]

    percentage = churn_rate * 100

    return (
        f"{churned} of {total} customers churned "
        f"({percentage:.1f}%)."
    )
