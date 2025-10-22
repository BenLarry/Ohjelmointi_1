from classes.auto import Auto

class SahkoAuto(Auto):
    def __init__(self, registration_number, top_speed, battery):
        self.battery = battery
        super().__init__(registration_number, top_speed)