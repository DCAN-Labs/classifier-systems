from unittest import TestCase

from src.detectors.woods1_detector import Woods1Detector
from src.environments.woods1 import Woods1


class TestWoods1Detector(TestCase):
    def test_get_encoded_features(self):
        environment = Woods1('./data/woods1.txt')
        environment.set_current_position([2, 4])
        detector = Woods1Detector(environment)
        actual_encoded_features = detector.get_encoded_features()
        expected_encoded_features = '0000000000101011'
        self.assertEqual(actual_encoded_features, expected_encoded_features)
