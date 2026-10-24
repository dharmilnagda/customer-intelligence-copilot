
import json

from customer_intelligence.cli import main


def test_cli_prints_json_summary(monkeypatch, capsys):
    monkeypatch.setattr(
        "sys.argv",
        ["cli.py"],
    )

    main()

    output = capsys.readouterr().out
    summary = json.loads(output)

    assert summary["total_customers"] == 10
    assert summary["churned_customers"] == 4
    assert summary["retained_customers"] == 6


def test_cli_answers_question(monkeypatch, capsys):
    monkeypatch.setattr(
        "sys.argv",
        ["cli.py", "--question", "What is our churn rate?"],
    )

    main()

    output = capsys.readouterr().out.strip()

    assert output == (
        "The customer churn rate is 40.0% "
        "(4 out of 10 customers)."
    )
