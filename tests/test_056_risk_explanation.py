import unittest

from readmission_signal_board.models import Record
from readmission_signal_board.scoring import score_record


class DepthCheck56(unittest.TestCase):
    def test_056_risk_explanation(self):
        record = Record(id="patient-056", exposure=87469, signal=0.517, urgency=1)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
