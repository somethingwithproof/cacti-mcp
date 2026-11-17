"""Public command-line behavior, including execution as a Python module."""

import os
import subprocess
import sys

import pytest

from cacti_mcp import __version__


@pytest.mark.parametrize('option', ['--help', '--version'])
def test_informational_options_do_not_require_credentials(option):
    env = {
        key: value
        for key, value in os.environ.items()
        if key not in {'CACTI_MCP_ENDPOINT', 'CACTI_MCP_TOKEN'}
    }
    result = subprocess.run(
        [sys.executable, '-m', 'cacti_mcp', option],
        env=env,
        capture_output=True,
        text=True,
        timeout=10,
    )
    assert result.returncode == 0
    assert result.stderr == ''
    expected = __version__ if option == '--version' else 'usage:'
    assert expected in result.stdout


def test_missing_endpoint_reports_usage_without_disclosing_token():
    token = 'a' * 64
    env = {**os.environ, 'CACTI_MCP_TOKEN': token}
    env.pop('CACTI_MCP_ENDPOINT', None)
    result = subprocess.run(
        [sys.executable, '-m', 'cacti_mcp'],
        env=env,
        capture_output=True,
        text=True,
        timeout=10,
    )
    assert result.returncode == 2
    assert result.stdout == ''
    assert 'CACTI_MCP_ENDPOINT' in result.stderr
    assert token not in result.stderr
