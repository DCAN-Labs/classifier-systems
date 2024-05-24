import pandas as pd


class ZerothLevelClassifierSystem:
    def __init__(self, environment, classifiers_file, detector):
        self.environment = environment
        self.classifiers = self.get_classifiers(classifiers_file)
        self.detector = detector

    def done(self):
        pass

    def run_one_cycle(self, old_action_set):
        features = self.detector.get_encoded_features()
        match_set = self.classifiers.get_match_set(features)
        highest_bidders = match_set.get_highest_bidders()
        action_set = highest_bidders.get_action_set()
        old_action_set = old_action_set.pay_highest_bidders(action_set)

        return old_action_set

    @staticmethod
    def get_classifiers(classifiers_file):
        df = pd.read_csv(classifiers_file, sep=':', names=['condition', 'message', 'strength'], dtype={'message': str})

        return df
