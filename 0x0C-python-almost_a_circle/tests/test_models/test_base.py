#!/usr/bin/python3
"""
    Unittest for Base class
"""
import unittest
from models.base import Base


class TestBaseclass(unittest.TestCase):
    """ Test cases Base class"""
    def setUp(self):
        """ test raise heigt"""
        self.inst = Base(5)

    def tearDown(self):
        """ test raise heigt"""
        Base._Base__nb_objects = 0

    def test_nb_objs_yes(self):
        """ test raise heigt"""
        self.assertEqual(self.inst._Base__nb_objects, 0)

    def test_nb_objs_no(self):
        """ test raise heigt"""
        self.inst = Base()
        self.assertEqual(self.inst._Base__nb_objects, 1)

    def test_id(self):
        """ test raise heigt"""
        self.assertEqual(self.inst.id, 5)
