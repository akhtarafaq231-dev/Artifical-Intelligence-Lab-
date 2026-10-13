
class StatefulAgent:
    def __init__(self):
        self.previous_mode = None

    def sensor(self, temp, occupied):
        self.temp = temp
        self.occupied = occupied

    def act(self):
        if not self.occupied:
            target_mode = "ECO"
        elif self.temp > 26:
            target_mode = "COOL"
        elif self.temp < 20:
            target_mode = "WARM"
        else:
            target_mode = "IDLE"

        previous_mode = self.previous_mode
        send_command = target_mode != previous_mode

        if send_command:
            self.previous_mode = target_mode

        return previous_mode, target_mode, send_command