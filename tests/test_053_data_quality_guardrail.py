import unittest

from readmission_signal_board.models import Record
from readmission_signal_board.scoring import score_record


class DepthCheck53(unittest.TestCase):
    def test_053_data_quality_guardrail(self):
        record = Record(id="patient-053", exposure=73847, signal=0.405, urgency=7)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
