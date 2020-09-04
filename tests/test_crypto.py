"""
Tests for python/crypto.py
"""
import python
from python import *
import unittest
from unittest.mock import patch

class TestCrpyto(unittest.TestCase):

    @patch('vim.eval')
    def test_get_query_id_ticker(self):
        eval_mock.return_value = 'ticker'
        self.assertEqual('bitcoin', crypto._get_query_id('btc'))
        self.assertEqual(eval_mock, call_count, 1)


    def test_get_query_id_name(self):
        self.assertEqual(1,1)

