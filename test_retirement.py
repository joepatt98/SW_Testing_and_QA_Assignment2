import unittest

import retirement

class RetirementTest(unittest.TestCase):

    def test_retirement_calculate(self):
        self.assertEqual(retirement.Calculate_Retirement(22,76000,0.1,500000), 70)
