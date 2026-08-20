"""Unit 10 — cross-organisation digest."""

from app.digest import digest
from app.llm import FakeLLM
from tests.helpers import build_empty_index, build_test_index


def test_digest_covers_multiple_organisations(tmp_path):
    llm = FakeLLM("Org A restores soil [org-a-about]. Org B maps [org-b-about].")
    result = digest("weekly", build_test_index(tmp_path), llm, k=10)
    assert set(result.cited_source_ids) == {"org-a-about", "org-b-about"}


def test_digest_uses_the_digest_prompt_version(tmp_path):
    llm = FakeLLM("A [org-a-about].")
    result = digest("weekly", build_test_index(tmp_path), llm, k=10)
    assert result.prompt_version == "prompts/digest.md"


def test_digest_records_its_scope(tmp_path):
    llm = FakeLLM("A [org-a-about].")
    result = digest("weekly", build_test_index(tmp_path), llm, k=10)
    assert result.question_or_digest_scope == "weekly"


def test_digest_on_empty_index_is_insufficient(tmp_path):
    llm = FakeLLM("never returned")
    result = digest("weekly", build_empty_index(tmp_path), llm, k=10)
    assert result.insufficient_evidence is True
    assert llm.call_count == 0


def test_digest_rejects_unknown_citations(tmp_path):
    llm = FakeLLM("A claim [invented-source].")
    result = digest("weekly", build_test_index(tmp_path), llm, k=10)
    assert "invented-source" not in result.cited_source_ids
    assert result.limitations


def test_digest_records_usage(tmp_path):
    llm = FakeLLM("A [org-a-about].")
    result = digest("weekly", build_test_index(tmp_path), llm, k=10)
    assert result.usage.input_tokens > 0
