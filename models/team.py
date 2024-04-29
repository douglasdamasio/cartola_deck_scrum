

class Team:
    def __init__(self, id: int, team_name: str, player_name: str, 
                 points_championship: float, points_round: float, 
                 patrimony: float, pro: bool):
        self.id = id
        self.team_name = team_name
        self.player_name = player_name
        self.points_championship = points_championship
        self.points_round = points_round
        self.patrimony = patrimony
        self.pro = pro

    def __repr__(self):
        return "<Team %r>" % self.nome
    
    def serialize(self) -> dict:
        return {
            'id': self.id,
            'team_name': self.team_name,
            'player_name': self.player_name,
            'points_championship': self.points_championship,
            'points_round': self.points_round,
            'patrimony': self.patrimony,
            'pro': self.pro
        }
