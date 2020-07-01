#!/usr/bin/python3
""" Unit testing City class """

import os
import unittest
from models.city import City
from datetime import datetime
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """ Class to make unit testing for City class """

    def setUp(self):
        """ setUp method that executes before each test method """

        self.City1 = City()
        self.City1.state_id = "760041"
        self.City1.name = "Santiago de Cali"

    def tearDown(self):
        """ tearDown method that executes after each test method """

        del self.City1

        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_attributes(self):
        """ testing the attributes of City Class """

        attr = self.City1.to_dict()

        """ testing if the attributes exists in the instance """
        self.assertTrue('name' in attr)
        self.assertTrue('state_id' in attr)
        self.assertTrue('created_at' in attr)
        self.assertTrue('updated_at' in attr)
        self.assertTrue('id' in attr)
        self.assertTrue('__class__' in attr)

        """ testing the types of the attributes """
        self.assertIsInstance(self.City1.name, str)
        self.assertIsInstance(self.City1.state_id, str)
        self.assertIsInstance(self.City1.id, str)
        self.assertIsInstance(self.City1.created_at, datetime)
        self.assertIsInstance(self.City1.updated_at, datetime)

    def test_inheritance(self):
        """ Testing if City class inherits from BaseModel class """

        self.assertIsInstance(self.City1, BaseModel)

    def test_permissions(self):
        """ testing permissions of the file City.py """

        file = 'models/city.py'
        self.assertTrue(os.access(file, os.R_OK))
        self.assertTrue(os.access(file, os.W_OK))
        self.assertTrue(os.access(file, os.X_OK))


if __name__ == "__main__":
    """ if it's executed as main program """

    unittest.main()
