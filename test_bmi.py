import unittest

import bmi

class BMITest(unittest.TestCase):

    def test_bmi_height(self):

        self.assertEqual(bmi.Height(0,1), 0.025)
        self.assertEqual(bmi.Height(6,2), 1.85)
        self.assertEqual(bmi.Height(12,4), 3.7)

    def test_bmi_weight(self):

        self.assertEqual(bmi.Weight(0), 0)
        self.assertEqual(bmi.Weight(200), 90)
        self.assertEqual(bmi.Weight(400.33333), 180.1499985)

    def test_bmi_calculate_bmi(self):

        self.assertEqual(bmi.Calculate_BMI(0.33333, 0.33333), 3)
        self.assertEqual(bmi.Calculate_BMI(2, 100), 25)
        self.assertEqual(bmi.Calculate_BMI(3.33333, 200.33333), 18)

    def test_bmi_calculate_category(self):

        self.assertEqual(bmi.Calculate_Category(0), "Underweight")
        self.assertEqual(bmi.Calculate_Category(18.4), "Underweight")
        self.assertEqual(bmi.Calculate_Category(18.5), "Normal weight")
        self.assertEqual(bmi.Calculate_Category(24.9), "Normal weight")
        self.assertEqual(bmi.Calculate_Category(25), "Overweight")
        self.assertEqual(bmi.Calculate_Category(29.9), "Overweight")
        self.assertEqual(bmi.Calculate_Category(30), "Obese")
        self.assertEqual(bmi.Calculate_Category(100), "Obese")
