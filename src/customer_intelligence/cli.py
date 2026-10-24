
import argparse
import json
from pathlib import Path

import pandas as pd

from customer_intelligence.customer_analytics import (
    calculate_churn_summary,
)
from customer_intelligence.customer_insights import summarize_churn
from customer_intelligence.question_answering import answer_question


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate customer analytics and answer questions."
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("data/customers.csv"),
        help="Path to a customer CSV file.",
    )
    parser.add_argument(
        "--question",
        type=str,
        help="Ask a question about the customer data.",
    )

    args = parser.parse_args()
    customers = pd.read_csv(args.input)

    if args.question:
        answer = answer_question(args.question, customers)
        print(answer)
        return

    summary = calculate_churn_summary(customers)
    summary["business_summary"] = summarize_churn(summary)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
