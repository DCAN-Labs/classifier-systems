class Woods1Detector:
    def __init__(self, woods1):
        self.woods1 = woods1

    def get_encoded_features(self):
        current_position = self.woods1.get_current_position()
        encoded_features = ''
        relative_postions = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
        for relative_position in relative_postions:
            current_token_pos = \
                [(current_position[0] + relative_position[0] + self.woods1.get_height()) % self.woods1.get_height(),
                 (current_position[1] + relative_position[1] + self.woods1.get_width()) % self.woods1.get_width()]
            if self.woods1.world[current_token_pos[0]][current_token_pos[1]] == 'F':
                encoded_features += '11'
            elif self.woods1.world[current_token_pos[0]][current_token_pos[1]] == 'O':
                encoded_features += '10'
            else:
                encoded_features += '00'

        return encoded_features
