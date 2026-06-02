import pytest


def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "github_io: live checks for shahzebqazi.github.io redirect stubs",
    )
