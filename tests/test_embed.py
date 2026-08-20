"""Unit 5 — the embedder interface and its deterministic fake."""

import pytest

from app.embed import FakeEmbedder


def test_fake_embedder_returns_one_vector_per_text():
    vectors = FakeEmbedder(dim=8).embed(["alpha", "beta", "gamma"])
    assert len(vectors) == 3


def test_fake_embedder_respects_requested_dimension():
    vectors = FakeEmbedder(dim=8).embed(["alpha"])
    assert len(vectors[0]) == 8


def test_fake_embedder_is_deterministic():
    assert FakeEmbedder(dim=8).embed(["alpha"]) == FakeEmbedder(dim=8).embed(["alpha"])


def test_different_text_produces_different_vectors():
    embedder = FakeEmbedder(dim=8)
    assert embedder.embed(["alpha"])[0] != embedder.embed(["beta"])[0]


def test_vectors_are_unit_length():
    vector = FakeEmbedder(dim=8).embed(["alpha"])[0]
    magnitude = sum(value * value for value in vector) ** 0.5
    assert magnitude == pytest.approx(1.0, abs=1e-6)


def test_empty_input_returns_empty_list():
    assert FakeEmbedder(dim=8).embed([]) == []


def test_embedder_reports_its_model_identifier():
    assert FakeEmbedder(dim=8).model_id == "fake-embedder-8"
