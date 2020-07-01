#!/usr/bin/python3
""" Unit testing place class """

import os
import unittest
from models.place import Place
from datetime import datetime
from models.base_model import BaseModel


class Testplace(unittest.TestCase):
    """ Class to make unit testing for place class """

    def setUp(self):
        """ setUp method that executes before each test method """

        self.place1 = Place()
        self.place1.city_id = "234g894u9238h9"
        self.place1.user_id = "35839488h9309rj"
        self.place1.name = "CocoBay"
        self.place1.description = "House located in San Andres"
        self.place1.number_rooms = 4
        self.place1.number_bathrooms = 2
        self.place1.max_guest = 6
        self.place1.price_by_night = 30
        self.place1.latitude = 123454354.68
        self.place1.longitude = 43565423.67
        self.place1.amenity_ids = ['pool']

    def tearDown(self):
        """ tearDown method that executes after each test method """

        del self.place1

        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_attributes(self):
        """ testing the attributes of place Class """

        attr = self.place1.to_dict()

        """ testing if the attributes exists in the instance """
        self.assertTrue('city_id' in attr)
        self.assertTrue('user_id' in attr)
        self.assertTrue('name' in attr)
        self.assertTrue('description' in attr)
        self.assertTrue('number_rooms' in attr)
        self.assertTrue('number_bathrooms' in attr)
        self.assertTrue('max_guest' in attr)
        self.assertTrue('price_by_night' in attr)
        self.assertTrue('latitude' in attr)
        self.assertTrue('longitude' in attr)
        self.assertTrue('amenity_ids' in attr)
        self.assertTrue('created_at' in attr)
        self.assertTrue('updated_at' in attr)
        self.assertTrue('id' in attr)
        self.assertTrue('__class__' in attr)

        """ testing the types of the attributes """
        self.assertIsInstance(self.place1.city_id, str)
        self.assertIsInstance(self.place1.user_id, str)
        self.assertIsInstance(self.place1.name, str)
        self.assertIsInstance(self.place1.description, str)
        self.assertIsInstance(self.place1.number_rooms, int)
        self.assertIsInstance(self.place1.number_bathrooms, int)
        self.assertIsInstance(self.place1.max_guest, int)
        self.assertIsInstance(self.place1.price_by_night, int)
        self.assertIsInstance(self.place1.latitude, float)
        self.assertIsInstance(self.place1.longitude, float)
        self.assertIsInstance(self.place1.amenity_ids, list)
        self.assertIsInstance(self.place1.id, str)
        self.assertIsInstance(self.place1.created_at, datetime)
        self.assertIsInstance(self.place1.updated_at, datetime)

    def test_inheritance(self):
        """ Testing if place class inherits from BaseModel class """

        self.assertIsInstance(self.place1, BaseModel)

    def test_permissions(self):
        """ testing permissions of the file place.py """

        file = 'models/place.py'
        self.assertTrue(os.access(file, os.R_OK))
        self.assertTrue(os.access(file, os.W_OK))
        self.assertTrue(os.access(file, os.X_OK))


if __name__ == "__main__":
    """ if it's executed as main program """

    unittest.main()
