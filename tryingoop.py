class GameSession:
    max_score = 1000

    def __init__(self, player_name):
        self.player_name = player_name
        self.score = 0
        self.is_active = True

    def add_score(self, points):
        self.score += points
        print(f"Score for {self.player_name}: {self.score}")

    def end_session(self):
        self.is_active = False
        print(f"Session ended for {self.player_name}")

    def status(self):
        state = "Active" if self.is_active else "Ended"
        print(f"{state} | Score: {self.score}")

    @classmethod
    def set_max_score(cls, new_max):
        cls.max_score = new_max
        print(f"Max score is now {cls.max_score}")

    @staticmethod
    def is_valid_name(name):
        if len(name) <= 2:
            return False
        for char in name:
            if char.isdigit():
                return False
        return True