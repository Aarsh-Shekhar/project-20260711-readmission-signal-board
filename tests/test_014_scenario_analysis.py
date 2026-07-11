import unittest

from readmission_signal_board.models import Record
from readmission_signal_board.scoring import score_record


class DepthCheck14(unittest.TestCase):
    def test_014_scenario_analysis(self):
        record = Record(id="patient-014", exposure=60910, signal=0.778, urgency=7)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
