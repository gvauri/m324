import os
from unittest import TestCase

from file import File


class TestFile(TestCase):
    testee: File

    def setUp(self):
        self.testee = File()

    def test_read_from_file(self):
        filename = "./create_file.txt"
        text = "Hello World"
        with open(filename, "w") as f:
            f.write(text)

        actual_text = self.testee.read_from_file(filename)

        self.assertEqual(text, actual_text, msg="text assertion")
        os.remove(filename)

    def test_write_to_file(self):
        filename = "./create_file.txt"
        text = "Hello World"

        self.testee.write_to_file(filename, text)

        self.assertTrue(os.path.exists(filename), msg="File was not created")
        with open(filename, "r") as f:
            self.assertEqual(text, f.read(), msg="text assertion")
        os.remove(filename)

    def test_create_file(self):
        filename = "./create_file.txt"

        self.testee.create_file(filename)

        self.assertTrue(os.path.exists(filename), msg="File was not created")
        os.remove(filename)
