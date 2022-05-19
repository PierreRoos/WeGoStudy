import unittest
import WeGoStudy_locators as locators
import WeGoStudy_methods as methods

class PositiveTestCases(unittest.TestCase):
    @staticmethod
    def test_create_new_user():
        methods.setUp()
        methods.login()
        methods.create_new_student()
        methods.create_new_application()
        methods.view_details()
        methods.logout()
        methods.tearDown()
        