from ex2 import exercice_2
import unittest
 
class Exercice_2_test_case(unittest.TestCase):

    def test_inf(self):
        self.assertEqual(exercice_2(-5, -2, 5), -255)
        self.assertEqual(exercice_2(-10, 0, 5), -255)
        self.assertEqual(exercice_2(-1, 0, 5), -255)

    def test_sup(self):
        self.assertEqual(exercice_2(8, -2, 5), 255)
        self.assertEqual(exercice_2(10, 0, 8), 255)
        self.assertEqual(exercice_2(-1, 0, 5), 255)
        
    def test_inter(self):
        self.assertEqual(exercice_2(2, -2, 5), -2)
        self.assertEqual(exercice_2(-3, -6, 0), -3)
        self.assertEqual(exercice_2(0, 0, 0), 0)
        self.assertEqual(exercice_2(1, 1, 5), 1)


    def test_borne(self):
        self.assertRaises(ValueError, exercice_2, 5, 3, 2)
        self.assertRaises(ValueError, exercice_2, -5, 0, 2)
