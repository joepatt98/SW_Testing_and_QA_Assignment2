import unittest

import retirement

class RetirementTest(unittest.TestCase):

    def test_retirement_calculate_retirement(self):

        self.assertEqual(retirement.Calculate_Retirement(22, 76000, 0.1, 500000), 71)
        self.assertEqual(retirement.Calculate_Retirement(25, 65000, 0.1, 1500000), 196)
        self.assertEqual(retirement.Calculate_Retirement(45, 100000, 0.15, 500000), 70)

    def test_retirement_output(self):

        self.assertEqual(retirement.Output(71), "\nGoal will be met at ")
        self.assertEqual(retirement.Output(99.9), "\nGoal will be met at ")
        self.assertEqual(retirement.Output(100), "\nDeath will occur before goal is met at ")
        self.assertEqual(retirement.Output(196), "\nDeath will occur before goal is met at ")
