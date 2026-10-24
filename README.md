# Customer Intelligence Copilot

A production-minded customer analytics project that combines reliable Python analytics, business-friendly insights, and rule-based question answering as a foundation for a grounded AI assistant.

## Current Features

- Calculate customer churn, retention, and churn rate.
- Generate concise business summaries.
- Answer supported questions about customer metrics.
- Load customer data from a CSV file.
- Validate inputs and handle unsupported questions.
- Automated tests for analytics, insights, question answering, and CLI behavior.

## Tech Stack

- Python 3.12
- pandas
- pytest
- uv

## Getting Started

Clone the repository and install the dependencies:

```bash
uv sync
```

Run the customer analytics summary:

```bash
uv run python -m customer_intelligence.cli
```

Ask a question about customer churn:

```bash
uv run python -m customer_intelligence.cli --question "What is our churn rate?"
```

Use a different CSV file:

```bash
uv run python -m customer_intelligence.cli --input path/to/customers.csv
```

Run the test suite:

```bash
uv run pytest -v
```

## Sample Data

The repository includes a small synthetic customer dataset for demonstration and testing. Its results should not be interpreted as real-world customer churn estimates.

## Current Limitations

Question answering currently supports a limited set of predefined question patterns. It does not yet use an LLM, retrieval-augmented generation (RAG), or external knowledge sources.

## Planned Development

- Improve data validation and analytics coverage.
- Introduce grounded retrieval and question answering.
- Explore LLM integration and evaluation.
- Add production-oriented reliability, observability, and deployment practices.