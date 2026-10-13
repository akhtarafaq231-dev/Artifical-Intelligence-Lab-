
class SimpleReflexAgent:
    def sensor(self, temp, occupied):
        self.temp = temp
        self.occupied = occupied

    def act(self):
        if not self.occupied:
            return "ECO"
        elif self.temp > 26:
            return "COOL"
        elif self.temp < 20:
            return "WARM"
        else:
            return "IDLE"


agent = SimpleReflexAgent()

percepts = [
    (29, True),
    (29, True),
    (20, True),
    (26, True),
    (19, True),
    (29, False)
]

for temp, occupied in percepts:
    agent.sensor(temp, occupied)
    print((temp, occupied), "Target mode:", agent.act())