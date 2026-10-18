
import argparse
import json
from pathlib import Path

import pandas as pd

from customer_intelligence.customer_analytics import (
    calculate_churn_summary,
)
from customer_intelligence.customer_insights import summarize_churn


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate a customer churn summary."
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("data/customers.csv"),
        help="Path to a customer CSV file.",
    )
    args = parser.parse_args()

    customers = pd.read_csv(args.input)
    summary = calculate_churn_summary(customers)
    summary["business_summary"] = summarize_churn(summary)

    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
