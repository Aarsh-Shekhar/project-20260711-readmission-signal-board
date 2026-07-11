import unittest

from readmission_signal_board.models import Record
from readmission_signal_board.scoring import score_record


class DepthCheck47(unittest.TestCase):
    def test_047_control_mapping(self):
        record = Record(id="patient-047", exposure=18823, signal=0.864, urgency=5)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
