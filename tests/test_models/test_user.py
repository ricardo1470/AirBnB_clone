#!/usr/bin/python3
""" Unit testing User class """

import os
import unittest
from models.user import User
from datetime import datetime
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """ Class to make unit testing for User class """

    def setUp(self):
        """ setUp method that executes before each test method """

        self.user1 = User()
        self.user1.email = "plantita@example.com"
        self.user1.password = "laratacomequeso123"
        self.user1.first_name = "Noe"
        self.user1.last_name = "Plantita"

    def tearDown(self):
        """ tearDown method that executes after each test method """

        del self.user1

        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_attributes(self):
        """ testing the attributes of User Class """

        attr = self.user1.to_dict()

        """ testing if the attributes exists in the instance """
        self.assertTrue('email' in attr)
        self.assertTrue('password' in attr)
        self.assertTrue('first_name' in attr)
        self.assertTrue('last_name' in attr)
        self.assertTrue('created_at' in attr)
        self.assertTrue('updated_at' in attr)
        self.assertTrue('id' in attr)
        self.assertTrue('__class__' in attr)

        """ testing the types of the attributes """
        self.assertIsInstance(self.user1.email, str)
        self.assertIsInstance(self.user1.password, str)
        self.assertIsInstance(self.user1.first_name, str)
        self.assertIsInstance(self.user1.last_name, str)
        self.assertIsInstance(self.user1.id, str)
        self.assertIsInstance(self.user1.created_at, datetime)
        self.assertIsInstance(self.user1.updated_at, datetime)

    def test_inheritance(self):
        """ Testing if User class inherits from BaseModel class """

        self.assertIsInstance(self.user1, BaseModel)

    def test_permissions(self):
        """ testing permissions of the file user.py """

        file = 'models/user.py'
        self.assertTrue(os.access(file, os.R_OK))
        self.assertTrue(os.access(file, os.W_OK))
        self.assertTrue(os.access(file, os.X_OK))


if __name__ == "__main__":
    """ if it's executed as main program """

    unittest.main()
