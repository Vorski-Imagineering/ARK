"""Unit 9a — the citation contract."""

from app.answer import answer
from app.llm import FakeLLM
from tests.helpers import build_test_index


def test_answer_extracts_cited_source_ids(tmp_path):
    llm = FakeLLM("Org A restores soil [org-a-about].")
    result = answer("What does Org A do?", build_test_index(tmp_path), llm, k=3)
    assert result.cited_source_ids == ["org-a-about"]


def test_every_citation_resolves_to_a_source_in_the_index(tmp_path):
    index = build_test_index(tmp_path)
    llm = FakeLLM("Claim one [org-a-about]. Claim two [org-b-about].")
    result = answer("q", index, llm, k=3)
    known = {c.source_id for c in index.all()}
    for source_id in result.cited_source_ids:
        assert source_id in known


def test_citation_to_unknown_source_is_rejected(tmp_path):
    llm = FakeLLM("A fabricated claim [not-a-real-source].")
    result = answer("q", build_test_index(tmp_path), llm, k=3)
    assert "not-a-real-source" not in result.cited_source_ids
    assert result.limitations


def test_answer_records_usage(tmp_path):
    llm = FakeLLM("Org A restores soil [org-a-about].")
    result = answer("q", build_test_index(tmp_path), llm, k=3)
    assert result.usage.input_tokens > 0
    assert result.usage.output_tokens > 0
    assert result.usage.estimated_cost_usd >= 0


def test_answer_records_model_and_prompt_version(tmp_path):
    llm = FakeLLM("Org A restores soil [org-a-about].", model_id="fake-model-1")
    result = answer("q", build_test_index(tmp_path), llm, k=3)
    assert result.model == "fake-model-1"
    assert result.prompt_version == "prompts/answer.md"


def test_answer_starts_unreviewed(tmp_path):
    llm = FakeLLM("Org A restores soil [org-a-about].")
    result = answer("q", build_test_index(tmp_path), llm, k=3)
    assert result.review_status == "unreviewed"


def test_duplicate_citations_are_deduplicated_in_order(tmp_path):
    llm = FakeLLM("A [org-a-about]. B [org-b-about]. C [org-a-about].")
    result = answer("q", build_test_index(tmp_path), llm, k=3)
    assert result.cited_source_ids == ["org-a-about", "org-b-about"]
