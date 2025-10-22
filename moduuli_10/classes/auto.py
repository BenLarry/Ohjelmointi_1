class Auto():
    def __init__(self, registration_number, top_speed):
        self.registration_number = registration_number
        self.top_speed = top_speed
        self.current_speed = 0
        self.travel_distance = 0

    def accelerate(self, speed):
        new_speed = self.current_speed + speed
        if new_speed <= 0:
            self.current_speed = 0
        elif new_speed >= self.top_speed:
            self.current_speed = self.top_speed
        else:
            self.current_speed += speed

    def drive(self, time):
        self.travel_distance += self.current_speed * time

    def __str__(self):
        return f"NM: {self.registration_number}, CS: {self.current_speed} TS: {self.top_speed}, DIST: {self.travel_distance}"