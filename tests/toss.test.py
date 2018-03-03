import unittest
import sys
import imp
imp.load_source('toss','../toss.py')
from toss import take_decision


class TossTest(unittest.TestCase):

    def test_clear_day(self):
        team, decision = take_decision('day', 'clear')
        if team == "enchai":
            self.assertEqual(decision.lower(), "bowls")
        else:
            self.assertEqual(decision.lower(), "bats")    

    def test_cloudy_night(self):
        team, decision = take_decision('night', 'cloudy')
        if team == "enchai":
            self.assertEqual(decision.lower(), "bats")
        else:
            self.assertEqual(decision.lower(), "bowls")

    def test_clear_night(self):
        team, decision = take_decision('night', 'clear')
        if decision.lower() in ["bats","bowls"]:
            self.assertTrue(True)
        
      
if __name__ == '__main__':
    unittest.main()            

