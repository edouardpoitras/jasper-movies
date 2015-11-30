# -*- coding: utf-8 -*-
import unittest
from client import testutils
from . import movies


class TestMoviesPlugin(unittest.TestCase):
    def setUp(self):
        self.plugin = testutils.get_plugin_instance(movies.MoviesPlugin)

    def test_is_valid_method(self):
        self.assertTrue(self.plugin.is_valid("Jasper, tell me about some movies"))
        self.assertTrue(self.plugin.is_valid("movie"))
        self.assertFalse(self.plugin.is_valid("Jasper, you're the best!"))
