import enum
from constants import DOUGLAS_TEAM_ID, RENAN_TEAM_ID, THIAGO_TEAM_ID
from exceptions import TeamNotFound
from models.team import Team
from services import CartolaService


class TeamIds(enum.Enum):
    DOUGLAS = DOUGLAS_TEAM_ID
    RENAN = RENAN_TEAM_ID
    THIAGO = THIAGO_TEAM_ID


class DataSourceTeam:

    @staticmethod
    def get_team_id(player_nickname: str) -> int:
        player_team_id = {team.name: team.value for team in TeamIds}
        try:
            return player_team_id[player_nickname.upper()]
        except KeyError:
            raise TeamNotFound(f'Time do {player_nickname} não encontrado')

    @staticmethod
    def get_team(team_id: int) -> Team:
        return CartolaService().get_team_details(team_id)
    
    @classmethod
    def get_team_by_nickname(cls, player_nickname: str) -> Team:
        team_id = cls.get_team_id(player_nickname)
        return cls.get_team(team_id)

    @staticmethod
    def get_all_teams() -> list[Team]:
        return [
            CartolaService()
            .get_team_details(team.value)
            for team in TeamIds
        ]
