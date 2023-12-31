
import unittest
from score_system import ScoreSystem

class TestScoreSystem(unittest.TestCase):
    def setUp(self):
        self.score_system = ScoreSystem()

    def test_initial_score(self):
        self.assertEqual(self.score_system.get_total_score(), 0)
        self.assertEqual(self.score_system.get_average_score(), 0)

    def test_update_score(self):
        self.score_system.update_score(10)
        self.assertEqual(self.score_system.get_total_score(), 10)
        self.assertEqual(self.score_system.get_average_score(), 10)

        self.score_system.update_score(20)
        self.assertEqual(self.score_system.get_total_score(), 30)
        self.assertEqual(self.score_system.get_average_score(), 15)

    def test_reset_score(self):
        self.score_system.update_score(10)
        self.score_system.update_score(20)
        self.score_system.reset_score()
        self.assertEqual(self.score_system.get_total_score(), 0)
        self.assertEqual(self.score_system.get_average_score(), 0)

if __name__ == '__main__':
    unittest.main()

