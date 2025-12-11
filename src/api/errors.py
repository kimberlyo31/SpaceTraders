# src/api/errors.py
class ShipCooldownError(Exception):
    def __init__(self, cooldown_data):
        self.cooldown = cooldown_data
        super().__init__(f"Ship on cooldown: {cooldown_data['remainingSeconds']}s remaining")
