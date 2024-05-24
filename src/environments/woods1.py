from src.environments.environment import Environment


class Woods1(Environment):
    def __init__(self, environment_file):
        self.environment_file = environment_file
        with open(self.environment_file) as file:
            lines = [line.rstrip() for line in file]
            for i in range(len(lines)):
                line = lines[i]
                if line.startswith('#'):
                    continue
                else:
                    parts = line.split()
                    self.width = int(parts[0])
                    self.height = int(parts[1])
                    self.world = [["" for i in range(self.width)] for _ in range(self.height)]
                    i += 2
                    for row in range(self.height):
                        line = lines[i]
                        for col in range(self.width):
                            self.world[row][col] = line[col]
                        i += 1
                    break

