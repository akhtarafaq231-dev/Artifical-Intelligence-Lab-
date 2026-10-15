"""Lab 2 - Task 3 (guided): Simple Reflex Agent.
Sir ke pattern mein: sensor() + act().
Run: python lab2_percepts.py
"""


class SimpleReflexAgent:
    def __init__(self):
        self.c_t = 0
        self.occupied = False

    def sensor(self, temp, occupied):
        self.c_t = temp
        self.occupied = occupied

    def act(self):
        if not self.occupied:
            print("ECO mode")
        elif self.c_t > 26:
            print("COOL mode")
        elif self.c_t < 20:
            print("WARM mode")
        else:
            print("IDLE mode")


agent = SimpleReflexAgent()
percepts = [(29, True), (29, True), (20, True),
            (26, True), (19, True), (29, False)]
for step, (temp, occupied) in enumerate(percepts, 1):
    agent.sensor(temp, occupied)
    print("Step", step, (temp, occupied), "->", end=" ")
    agent.act()
