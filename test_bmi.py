import unittest

import bmi

class BMITest(unittest.TestCase):

    def test_bmi_height(self):
        self.assertEqual(bmi.Height(6,2), 1.85)
