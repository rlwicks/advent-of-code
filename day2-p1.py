from dataclasses import dataclass
import math
import sys


class Game:
    COLOR_INDICES = {
        "red": 0,
        "green": 1,
        "blue": 2,
    }
    LEGAL_MAX_PER_COLOR = [12, 13, 14]

    def __init__(self, game_text: str):
        game_text = game_text.lower().strip()
        self.game_id = int(game_text.split(":")[0].strip().split(" ")[1])
        set_texts = game_text.split(":")[1].strip().split(";")
        # self.set_color_cnts = np.zeros(shape=[3, len(set_texts)])
        self.is_legal = True
        self.min_color_cnts = [0, 0, 0]
        for set_i, set_text in enumerate(set_texts):
            set_text = set_text.strip()
            color_texts = set_text.split(",")
            for c_t in color_texts:
                c_t = c_t.strip()
                cnt = int(c_t.split(" ")[0])
                c_i = self.COLOR_INDICES[c_t.split(" ")[1]]
                if cnt > self.LEGAL_MAX_PER_COLOR[c_i]:
                    self.is_legal = False
                self.min_color_cnts[c_i] = max(self.min_color_cnts[c_i], cnt)

    def is_legal(self):
        return self.is_legal

    def get_game_id(self):
        return self.game_id

    def get_power(self):
        return math.prod(self.min_color_cnts)


f = open(sys.argv[1], "r")
lines = f.readlines()

legal_game_id_sum = 0
powers_sum = 0
for line in lines:
    game = Game(line)
    if game.is_legal:
        legal_game_id_sum = legal_game_id_sum + game.get_game_id()
    powers_sum = powers_sum + game.get_power()
print("Part 1, legal ids sum: " + str(legal_game_id_sum))
print("Part 2, sum of powers: " + str(powers_sum))
