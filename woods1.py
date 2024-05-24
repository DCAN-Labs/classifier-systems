from environment import Environment


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
                    print(f'parts: {parts}')
                    self.width = int(parts[0])
                    self.height = int(parts[1])
                    self.world = [["" for i in range(self.width)] for j in range(self.height)]
                    print(f'world: {self.world}')
                    i += 2
                    for row in range(self.height):
                        line = lines[i]
                        print(f'line: {line}')
                        for col in range(self.width):
                            self.world[row][col] = line[col]
                        i += 1
                    print(f'self.world: {self.world}')
                    break

