"""Tests for testtools itself."""

# See README for copyright and licensing details.

import unittest


def test_suite():
    from testtools.tests import (
        test_compat,
        test_content,
        test_content_type,
        test_deferredruntest,
        test_fixturesupport,
        test_helpers,
        test_matchers,
        test_monkey,
        test_runtest,
        test_spinner,
        test_testtools,
        test_testresult,
        test_testsuite,
        )
    suites = []
    modules = [
        test_compat,
        test_content,
        test_content_type,
        test_deferredruntest,
        test_fixturesupport,
        test_helpers,
        test_matchers,
        test_monkey,
        test_runtest,
        test_spinner,
        test_testresult,
        test_testsuite,
        test_testtools,
        ]
    for module in modules:
        suites.append(getattr(module, 'test_suite')())
    return unittest.TestSuite(suites)
