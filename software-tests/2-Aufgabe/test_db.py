import copy
from unittest import TestCase

from db import *


class TestDB(TestCase):
    testee: DB

    def setUp(self):
        self.testee = DB("mongodb://localhost:27017")

    def tearDown(self):
        self.testee.close()

    def test_db(self):
        user = User("admin", "admin@localhost.com")

        self.testee.set_user(copy.deepcopy(user))
        actual = self.testee.get_user()

        self.assertEqual(actual.__dict__, user.__dict__)