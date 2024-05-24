from environment import Environment


class Woods1(Environment):
    def __init__(self, environment_file):
        self.environment_file = environment_file
        with open(self.environment_file) as file:
            lines = [line.rstrip() for line in file]
            for line in lines:
                if line.startswith('#'):
                    continue
                self.width, self.height = [int(part) for part in line.split()]
                print()
