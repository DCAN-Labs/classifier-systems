class Classifier:
    def __init__(self, condition, message, strength):
        self.condition = condition
        self.message = message
        self.strength = strength

    def matches(self, environment_state):
        pass
