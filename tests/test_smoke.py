"""Unit 0 — proves the package imports and the harness runs."""

import app


def test_package_imports():
    assert app.__version__ == "0.1.0"


def test_python_version_is_supported():
    import sys

    assert sys.version_info >= (3, 11)
