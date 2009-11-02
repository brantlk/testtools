# Copyright (c) 2008 Jonathan M. Lange. See LICENSE for details.

import sys
import unittest
from testtools.content import Content, TracebackContent
from testtools.content_type import ContentType


def test_suite():
    from unittest import TestLoader
    return TestLoader().loadTestsFromName(__name__)


class TestContent(unittest.TestCase):

    def test___init___None_errors(self):
        self.assertRaises(ValueError, Content, None, None)
        self.assertRaises(ValueError, Content, None, lambda:["traceback"])
        self.assertRaises(ValueError, Content,
            ContentType("text", "traceback"), None)

    def test___init___sets_ivars(self):
        content_type = ContentType("foo", "bar")
        content = Content(content_type, lambda:["bytes"])
        self.assertEqual(content_type, content.content_type)
        self.assertEqual(["bytes"], list(content.iter_bytes()))

    def test___eq__(self):
        content_type = ContentType("foo", "bar")
        content1 = Content(content_type, lambda:["bytes"])
        content2 = Content(content_type, lambda:["bytes"])
        content3 = Content(content_type, lambda:["by", "tes"])
        content4 = Content(content_type, lambda:["by", "te"])
        content5 = Content(ContentType("f","b"), lambda:["by", "tes"])
        self.assertEqual(content1, content2)
        self.assertEqual(content1, content3)
        self.assertNotEqual(content1, content4)
        self.assertNotEqual(content1, content5)


class TestTracebackContent(unittest.TestCase):

    def test___init___None_errors(self):
        self.assertRaises(ValueError, TracebackContent, None, None)

    def test___init___sets_ivars(self):
        exc_info = sys.exc_info()
        content = TracebackContent(exc_info, self)
        content_type = ContentType("text", "x-traceback",
            {"language":"python"})
        self.assertEqual(content_type, content.content_type)
        result = unittest.TestResult()
        expected = result._exc_info_to_string(exc_info, self)
        self.assertEqual(expected, ''.join(list(content.iter_bytes())))