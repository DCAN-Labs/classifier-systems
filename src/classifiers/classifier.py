class Classifier:
    def __init__(self, condition, action, strength):
        self.condition = condition
        self.action = action
        self.strength = strength

    def matches(self, environment_state):
        pass
