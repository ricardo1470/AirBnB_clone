#!/usr/bin/python3
""" Unit testing review class """

import os
import unittest
from models.review import Review
from datetime import datetime
from models.base_model import BaseModel


class Testreview(unittest.TestCase):
    """ Class to make unit testing for Review class """

    def setUp(self):
        """ setUp method that executes before each test method """

        self.review1 = Review()
        self.review1.name = "Plantita"

    def tearDown(self):
        """ tearDown method that executes after each test method """

        del self.review1

        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_attributes(self):
        """ testing the attributes of Review Class """

        attr = self.review1.to_dict()

        """ testing if the attributes exists in the instance """
        self.assertTrue('name' in attr)
        self.assertTrue('created_at' in attr)
        self.assertTrue('updated_at' in attr)
        self.assertTrue('id' in attr)
        self.assertTrue('__class__' in attr)

        """ testing the types of the attributes """
        self.assertIsInstance(self.review1.name, str)
        self.assertIsInstance(self.review1.id, str)
        self.assertIsInstance(self.review1.created_at, datetime)
        self.assertIsInstance(self.review1.updated_at, datetime)

    def test_inheritance(self):
        """ Testing if Review class inherits from BaseModel class """

        self.assertIsInstance(self.review1, BaseModel)

    def test_permissions(self):
        """ testing permissions of the file review.py """

        file = 'models/review.py'
        self.assertTrue(os.access(file, os.R_OK))
        self.assertTrue(os.access(file, os.W_OK))
        self.assertTrue(os.access(file, os.X_OK))


if __name__ == "__main__":
    """ if it's executed as main program """

    unittest.main()
