from classes.auto import Auto

class PolttoMoottoriAuto(Auto):
    def __init__(self, registration_number, top_speed, gas):
        self.gas = gas 
        super().__init__(registration_number, top_speed)