"""Unit 9b — refusing to answer without evidence."""

from app.answer import answer
from app.llm import FakeLLM
from tests.helpers import build_empty_index, build_test_index


def test_empty_index_produces_insufficient_evidence(tmp_path):
    llm = FakeLLM("This should never be returned.")
    result = answer("anything", build_empty_index(tmp_path), llm, k=3)
    assert result.insufficient_evidence is True


def test_empty_index_does_not_call_the_model(tmp_path):
    llm = FakeLLM("This should never be returned.")
    answer("anything", build_empty_index(tmp_path), llm, k=3)
    assert llm.call_count == 0


def test_model_refusal_is_surfaced_as_insufficient_evidence(tmp_path):
    llm = FakeLLM("INSUFFICIENT EVIDENCE\nClosest: [org-a-about]")
    result = answer("q", build_test_index(tmp_path), llm, k=3)
    assert result.insufficient_evidence is True


def test_refusal_still_reports_closest_sources(tmp_path):
    llm = FakeLLM("INSUFFICIENT EVIDENCE\nClosest: [org-a-about]")
    result = answer("q", build_test_index(tmp_path), llm, k=3)
    assert "org-a-about" in result.cited_source_ids


def test_supported_answer_is_not_marked_insufficient(tmp_path):
    llm = FakeLLM("Org A restores soil [org-a-about].")
    result = answer("q", build_test_index(tmp_path), llm, k=3)
    assert result.insufficient_evidence is False


def test_answer_with_no_citations_is_marked_as_limited(tmp_path):
    llm = FakeLLM("Org A does many things.")
    result = answer("q", build_test_index(tmp_path), llm, k=3)
    assert result.cited_source_ids == []
    assert result.limitations
