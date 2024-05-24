from unittest import TestCase

from src.environments.woods1 import Woods1

from src.classifiers.zeroth_level_classifier_system import ZerothLevelClassifierSystem
from detectors.woods1_detector import Woods1Detector


class TestZerothLevelClassifierSystem(TestCase):
    def test_run_one_cycle(self):
        environment = Woods1('./data/woods1.txt')
        classifiers_file = './data/woods1_classifiers.txt'
        detector = Woods1Detector(environment)
        zeroth_level_classifier_system = ZerothLevelClassifierSystem(environment, classifiers_file, detector)
        zeroth_level_classifier_system.run_one_cycle([])
