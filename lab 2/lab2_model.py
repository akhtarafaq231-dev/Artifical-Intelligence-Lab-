"""Lab 2 - Task 3: Stateful Simple Reflex Agent (yaaddasht wala).
Sir ke pattern mein: sensor() + act(), plus purane mode ki memory.
Same command dobara nahi bhejta.
Save as lab2_model.py. Run: python lab2_check.py
"""


class SimpleReflexAgent:
    def __init__(self):
        self.c_t = 0
        self.occupied = False
        self.prev_mode = None  # internal memory

    def sensor(self, temp, occupied):
        self.c_t = temp
        self.occupied = occupied

    def act(self):
        # --- target mode ---
        if not self.occupied:
            target = "ECO"
        elif self.c_t > 26:
            target = "COOL"
        elif self.c_t < 20:
            target = "WARM"
        else:
            target = "IDLE"

        # --- repeat avoid karo ---
        old = self.prev_mode
        send_command = (target != old)
        self.prev_mode = target
        return old, target, send_command
