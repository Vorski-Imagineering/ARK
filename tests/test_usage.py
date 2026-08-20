"""Unit 11 — usage and cost accounting."""

import json

from app.usage import Usage, estimate_cost, log_run


def test_cost_is_computed_from_the_rate_table():
    cost = estimate_cost(
        model="test-model",
        input_tokens=1_000_000,
        output_tokens=1_000_000,
        rates={"test-model": {"input_per_m": 1.0, "output_per_m": 6.0}},
    )
    assert cost == 7.0


def test_partial_million_tokens_scale_linearly():
    cost = estimate_cost(
        model="test-model",
        input_tokens=500_000,
        output_tokens=0,
        rates={"test-model": {"input_per_m": 1.0, "output_per_m": 6.0}},
    )
    assert cost == 0.5


def test_unknown_model_costs_zero_and_is_not_an_error():
    assert estimate_cost("mystery", 1000, 1000, rates={}) == 0.0


def test_log_run_appends_one_json_line(tmp_path):
    path = tmp_path / "runs.jsonl"
    usage = Usage(input_tokens=10, output_tokens=5, estimated_cost_usd=0.001)
    log_run(path, run_id="r1", model="m", usage=usage, kind="answer")
    log_run(path, run_id="r2", model="m", usage=usage, kind="digest")
    assert len(path.read_text().strip().splitlines()) == 2


def test_logged_line_contains_the_expected_fields(tmp_path):
    path = tmp_path / "runs.jsonl"
    usage = Usage(input_tokens=10, output_tokens=5, estimated_cost_usd=0.001)
    log_run(path, run_id="r1", model="m", usage=usage, kind="answer")
    record = json.loads(path.read_text().strip())
    assert record["run_id"] == "r1"
    assert record["model"] == "m"
    assert record["input_tokens"] == 10
    assert record["output_tokens"] == 5
    assert record["kind"] == "answer"


def test_log_never_records_prompt_or_output_text(tmp_path):
    path = tmp_path / "runs.jsonl"
    usage = Usage(input_tokens=10, output_tokens=5, estimated_cost_usd=0.001)
    log_run(path, run_id="r1", model="m", usage=usage, kind="answer")
    record = json.loads(path.read_text().strip())
    assert "prompt" not in record
    assert "output" not in record
    assert "question" not in record
