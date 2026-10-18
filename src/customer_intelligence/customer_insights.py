
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
