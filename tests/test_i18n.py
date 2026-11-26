"""Tests for 20-locale i18n support in cacti-mcp."""

import os
import re
import subprocess
import sys

import pytest

from cacti_mcp.i18n import (
    DEFAULT_LOCALE,
    SUPPORTED_LOCALES,
    detect_locale,
    get_locale,
    load_catalog,
    normalize_locale,
    set_locale,
    t,
)

PLACEHOLDER_RE = re.compile(r'\{[a-zA-Z0-9_]+\}')


@pytest.fixture(autouse=True)
def _reset_locale(monkeypatch):
    for var in ('LC_ALL', 'LC_MESSAGES', 'LANG'):
        monkeypatch.delenv(var, raising=False)
    set_locale(None)
    yield
    set_locale(None)


def test_supported_locales_count_and_load():
    assert len(SUPPORTED_LOCALES) == 20
    en = load_catalog(DEFAULT_LOCALE)
    assert len(en) > 0
    for locale in SUPPORTED_LOCALES:
        catalog = load_catalog(locale)
        assert set(catalog.keys()) == set(en.keys()), locale
        for key, en_val in en.items():
            assert catalog[key].strip(), (locale, key)
            assert sorted(PLACEHOLDER_RE.findall(catalog[key])) == sorted(
                PLACEHOLDER_RE.findall(en_val)
            ), (locale, key)
            assert 'kadupul' not in catalog[key].lower(), (locale, key)


@pytest.mark.parametrize(
    ('raw', 'expected'),
    [
        (None, 'en'),
        ('', 'en'),
        ('C', 'en'),
        ('POSIX', 'en'),
        ('C.UTF-8', 'en'),
        ('de_DE.UTF-8', 'de'),
        ('de_AT.UTF-8@euro', 'de'),
        ('zh_TW', 'zh-TW'),
        ('zh_HK.UTF-8', 'zh-TW'),
        ('zh_Hant_TW', 'zh-TW'),
        ('zh_CN.UTF-8', 'zh-CN'),
        ('zh', 'zh-CN'),
        ('pt_BR.UTF-8', 'pt-BR'),
        ('pt_PT', 'pt-BR'),
        ('uk_UA.UTF-8', 'uk'),
        ('xx_YY', 'en'),
    ],
)
def test_normalize_locale(raw, expected):
    assert normalize_locale(raw) == expected


def test_env_precedence_and_set_locale(monkeypatch):
    assert detect_locale() == 'en'
    monkeypatch.setenv('LANG', 'fr_FR.UTF-8')
    assert detect_locale() == 'fr'
    monkeypatch.setenv('LC_MESSAGES', 'ja_JP.UTF-8')
    assert detect_locale() == 'ja'
    monkeypatch.setenv('LC_ALL', 'de_DE.UTF-8')
    assert detect_locale() == 'de'
    assert detect_locale('es') == 'es'

    assert set_locale('uk') == 'uk'
    assert get_locale() == 'uk'
    assert set_locale(None) == 'de'
    assert get_locale() == 'de'


def test_default_english_and_fallback():
    assert (
        t('cli.description')
        == 'Serve Cacti MCP plugin abilities as MCP tools over stdio.'
    )
    assert t('nonexistent.key') == 'nonexistent.key'
    assert t('error.http_status', locale='de', status=503, detail='') != t(
        'error.http_status', locale='en', status=503, detail=''
    )


def test_cli_lang_flag_localizes_help():
    assert normalize_locale('zh-TW-u-nu-hanidec') == 'zh-TW'
    assert normalize_locale('zh-HK-x-private') == 'zh-TW'
    assert normalize_locale('zh-Hans-TW') == 'zh-CN'
    assert normalize_locale('x-private') == 'en'

    env = {
        k: v
        for k, v in os.environ.items()
        if k not in {'LC_ALL', 'LC_MESSAGES', 'LANG'}
    }
    de = subprocess.run(
        [sys.executable, '-m', 'cacti_mcp', '--lang', 'de', '--help'],
        env=env,
        capture_output=True,
        text=True,
        timeout=10,
    )
    repeated = subprocess.run(
        [
            sys.executable,
            '-m',
            'cacti_mcp',
            '--lang',
            'tr',
            '--lang',
            'uk',
            '--help',
        ],
        env=env,
        capture_output=True,
        text=True,
        timeout=10,
    )
    en = subprocess.run(
        [sys.executable, '-m', 'cacti_mcp', '--help'],
        env=env,
        capture_output=True,
        text=True,
        timeout=10,
    )
    assert de.returncode == 0
    assert repeated.returncode == 0
    assert en.returncode == 0
    assert ' '.join(t('cli.description', locale='de').split()) in ' '.join(
        de.stdout.split()
    )
    assert ' '.join(t('cli.description', locale='uk').split()) in ' '.join(
        repeated.stdout.split()
    )
    assert ' '.join(t('cli.description', locale='en').split()) in ' '.join(
        en.stdout.split()
    )
