

class Round:
    def __init__(self, current_round: int):
        self.current_round = current_round
    
    def __repr__(self):
        return "<Round %r>" % self.current_round
    
    def serialize(self) -> dict:
        return {
            'current_round': self.current_round
        }
