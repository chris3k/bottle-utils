#-*- coding: utf-8 -*-
"""
test_common.py: Unit tests for ``bottle_utils.common`` module

Bottle Utils
2014 Outernet Inc <hello@outernet.is>
All rights reserved
"""

from __future__ import unicode_literals

try:
    from unittest import mock
except ImportError:
    import mock

import bottle_utils.common as mod


MOD = 'bottle_utils.common.'


def test_to_unicode():
    assert mod.to_unicode(1) == '1'
    assert mod.to_unicode(b'foobar') == 'foobar'
    assert mod.to_unicode('foo') == 'foo'


def test_to_bytes():
    assert mod.to_bytes('foobar', 'latin1') == b'foobar'


def test_attr_escaping():
    assert mod.attr_escape('"bar"') == '&quot;bar&quot;'
    assert mod.attr_escape('/?q=foo&b=bar') == '/?q=foo&amp;b=bar'


def test_html_escaping():
    assert mod.html_escape('<foo>bar</foo>') == '&lt;foo&gt;bar&lt;/foo&gt;'


@mock.patch(MOD + 'request')
def test_full_url(request):
    request.urlparts.scheme = 'http'
    request.urlparts.hostname = 'foo'
    request.urlparts.port = None
    assert mod.full_url('/') == 'http://foo/'


@mock.patch(MOD + 'request')
def test_full_url(request):
    request.urlparts.scheme = 'https'
    request.urlparts.hostname = 'foo'
    request.urlparts.port = 9000
    assert mod.full_url('/bar/baz') == 'https://foo:9000/bar/baz'


def test_urlquote():
    s = 'This is a test'
    assert mod.urlquote(s) == 'This%20is%20a%20test'


def test_urlquote_unicode():
    s = 'Ово је тест'
    assert mod.urlquote(s) == ('%D0%9E%D0%B2%D0%BE%20%D1%98%D0%B5%20%D1%82%D0%B5'
                           '%D1%81%D1%82')

