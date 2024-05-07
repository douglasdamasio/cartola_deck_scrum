from flask import Flask, render_template
from datasources.team import DataSourceTeam
from exceptions import TeamNotFound
from services import CartolaService
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin
def msg_hello():
    return render_template('index.html')

@app.route('/teams')
@cross_origin
def show_teams():
    all_teams = DataSourceTeam.get_all_teams()
    
    ordered_teams = sorted(
        all_teams, 
        key=lambda x: x.points_championship,
        reverse=True
    )
    
    return [team.serialize() for team in ordered_teams]

@app.route('/team/<nickname>')
@cross_origin
def show_team_by_player_nickname(nickname):
    try:
        team = DataSourceTeam.get_team_by_nickname(nickname)
        return team.serialize()
    except TeamNotFound as e:
        return str(e), 404

@app.route('/round')
@cross_origin
def show_current_round():
    return CartolaService().get_current_round().serialize()
