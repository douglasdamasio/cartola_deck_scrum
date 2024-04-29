import requests

from constants import GAME_API_BASE_URL
from models.round import Round
from models.team import Team

class CartolaService:
    def __init__(self):
        self.url = GAME_API_BASE_URL
    
    def get_team_details(self, team_id):
        team_detail = requests.get(f'{self.url}/time/id/{team_id}')
        return Team(
            id=team_detail.json()['time']['time_id'],
            team_name=team_detail.json()['time']['nome'],
            player_name=team_detail.json()['time']['nome_cartola'],
            points_championship=team_detail.json()['pontos_campeonato'],
            points_round=team_detail.json()['pontos'],
            patrimony=team_detail.json()['patrimonio'],
            pro=team_detail.json()['time']['assinante']
        )

    def get_current_round(self):
        round_detail = requests.get(f'{self.url}/mercado/status')
        return Round(
            current_round=round_detail.json()['rodada_atual']
        )
