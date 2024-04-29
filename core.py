import requests

DOUGLAS_TEAM_ID = 249112
RENAN_TEAM_ID = 892402
THIAGO_TEAM_ID = 47843219

GAME_API_BASE_URL = "https://api.cartola.globo.com/"

MAX_LEN_TEAM_NAME = 20
SEPARATOR_LEN = 80

team_ids = [
    DOUGLAS_TEAM_ID,
    RENAN_TEAM_ID,
    THIAGO_TEAM_ID
]

team_detail_list = []
for team_id in team_ids:
    team_details = requests.get(f'{GAME_API_BASE_URL}/time/id/{team_id}')
    team_detail_list.append({
        'time': team_details.json()['time']['nome'],
        'nome': team_details.json()['time']['nome_cartola'],
        'pontos_campeonato': team_details.json()['pontos_campeonato'],
        'pontos_rodada': team_details.json()['pontos'],
        'patrimonio': team_details.json()['patrimonio'],
        'pro': team_details.json()['time']['assinante'],
        'rodada': team_details.json()['rodada_atual']
    })

championship = sorted(team_detail_list, key=lambda x: -x['pontos_campeonato'])
round_number = str(f'\033[35m{team_detail_list[0]["rodada"]}º RODADA\033[0m').center(SEPARATOR_LEN)
header = str("Pos\tTime".ljust(MAX_LEN_TEAM_NAME))
line_separator = f'\033[35m-\033[0m' * SEPARATOR_LEN
print(f'\n{round_number}')
print(line_separator)
print(f'\033[32m{header}\tPts\t\tUlt.Rod\t\tPatrimonio\033[0m')
print(line_separator)
for pos, team in enumerate(championship, 1):
    team_name = team['time'].ljust(MAX_LEN_TEAM_NAME)
    if team['pro']:
        team_name = f'\033[33m{team_name}\033[0m'
    print(f'{pos}.\t{team_name}\t{team["pontos_campeonato"]:.2f}\t\t{team["pontos_rodada"]:.2f}\t\tC$ {team["patrimonio"]:.2f}')
print(line_separator)


