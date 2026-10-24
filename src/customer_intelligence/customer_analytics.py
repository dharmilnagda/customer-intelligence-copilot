
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


def get_customer_status(
    customers: pd.DataFrame,
    customer_id: str,
) -> dict[str, str | int]:
    """Return the status of a specific customer."""
    if "customer_id" not in customers.columns:
        raise ValueError(
            "Customer data must contain a 'customer_id' column."
        )

    if "churn" not in customers.columns:
        raise ValueError(
            "Customer data must contain a 'churn' column."
        )

    if customers["customer_id"].isna().any():
        raise ValueError("Customer IDs cannot contain missing values.")

    if customers["customer_id"].duplicated().any():
        raise ValueError("Customer IDs must be unique.")

    if customers["churn"].isna().any():
        raise ValueError("The 'churn' column cannot contain missing values.")

    if not customers["churn"].isin([0, 1]).all():
        raise ValueError("The 'churn' column must contain only 0 and 1.")

    matching_customers = customers[
        customers["customer_id"] == customer_id
    ]

    if matching_customers.empty:
        raise ValueError(f"Customer '{customer_id}' was not found.")

    churn_value = int(matching_customers.iloc[0]["churn"])

    return {
        "customer_id": customer_id,
        "churn": churn_value,
        "status": "Churned" if churn_value == 1 else "Retained",
    }
