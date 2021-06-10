import random
import string

class Robot:
    def __init__(self):
        random.seed()
        self.reset()

    def reset(self):
        self.get_name()

    def get_name(self):
        text = []
        for _ in range(2):
            text.append(random.choice(string.ascii_uppercase))
        for _ in range(3):
            text.append(random.choice(string.digits))
        self.name = "".join(text)
