import requests
import os
from dotenv import load_dotenv

load_dotenv()

def premier_results():
    url = "https://api.football-data.org/v4/competitions/PL/matches"
    api = os.getenv("football_api").strip()
    headers = {
        'X-Auth-Token': api
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    matches = data['matches']
    for match in matches:
        home_team = match['homeTeam']['name']
        away_team = match['awayTeam']['name']
        score_home = match['score']['fullTime']['home']
        score_away = match['score']['fullTime']['away']
        print(f"{home_team} {score_home} - {score_away} {away_team}")
def premier_table():
    url = "https://api.football-data.org/v4/competitions/PL/standings"
    api = os.getenv("football_api").strip()
    headers = {
        'X-Auth-Token': api
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    standings = data['standings'][0]['table']
    for team in standings:
        position = team['position']
        name = team['team']['name']
        points = team['points']
        print(f"{position}. {name} - {points} points")

def champions_results():
    url = "https://api.football-data.org/v4/competitions/CL/matches"
    api = os.getenv("football_api").strip()
    headers = {
        'X-Auth-Token': api
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    matches = data['matches']
    for match in matches:
        home_team = match['homeTeam']['name']
        away_team = match['awayTeam']['name']
        score_home = match['score']['fullTime']['home']
        score_away = match['score']['fullTime']['away']
        if score_home is None or score_away is None:
            continue
        print(f"{home_team} {score_home} - {score_away} {away_team}")

def champions_table():
    url = "https://api.football-data.org/v4/competitions/CL/matches"
    api = os.getenv("football_api").strip()
    headers = {
        'X-Auth-Token': api
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    matches = data['matches']
    teams = {}
    for match in matches:
        home_team = match['homeTeam']['name']
        away_team = match['awayTeam']['name']
        if home_team not in teams:
            teams[home_team] = {'points': 0, 'matches': 0}
        if away_team not in teams:
            teams[away_team] = {'points': 0, 'matches': 0}
        score_home = match['score']['fullTime']['home']
        score_away = match['score']['fullTime']['away']
        if score_home is None or score_away is None:
            continue
        teams[home_team]['matches'] += 1
        teams[away_team]['matches'] += 1
        if score_home > score_away:
            teams[home_team]['points'] += 3
        elif score_home < score_away:
            teams[away_team]['points'] += 3
        else:
            teams[home_team]['points'] += 1
            teams[away_team]['points'] += 1
    sorted_teams = sorted(teams.items(), key=lambda x: x[1]['points'], reverse=True)
    for i, (team, stats) in enumerate(sorted_teams):
        print(f"{i + 1}. {team} - {stats['points']} points")

def serie_results():
    url = "https://api.football-data.org/v4/competitions/SA/matches"
    api = os.getenv("football_api").strip()
    headers = {
        'X-Auth-Token': api
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    matches = data['matches']
    for match in matches:
        home_team = match['homeTeam']['name']
        away_team = match['awayTeam']['name']
        score_home = match['score']['fullTime']['home']
        score_away = match['score']['fullTime']['away']
        if score_home is None or score_away is None:
            continue
        print(f"{home_team} {score_home} - {score_away} {away_team}")

def serie_table():
    url = "https://api.football-data.org/v4/competitions/SA/standings"
    api = os.getenv("football_api").strip()
    headers = {
        'X-Auth-Token': api
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    standings = data['standings'][0]['table']
    for team in standings:
        position = team['position']
        name = team['team']['name']
        points = team['points']
        print(f"{position}. {name} - {points} points")

def bundesliga_results():
    url = "https://api.football-data.org/v4/competitions/BL1/matches"
    api = os.getenv("football_api").strip()
    headers = {
        'X-Auth-Token': api
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    matches = data['matches']
    for match in matches:
        home_team = match['homeTeam']['name']
        away_team = match['awayTeam']['name']
        score_home = match['score']['fullTime']['home']
        score_away = match['score']['fullTime']['away']
        if score_home is None or score_away is None:
            continue
        print(f"{home_team} {score_home} - {score_away} {away_team}")

def bundesliga_table():
    url = "https://api.football-data.org/v4/competitions/BL1/standings"
    api = os.getenv("football_api").strip()
    headers = {
        'X-Auth-Token': api
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    standings = data['standings'][0]['table']
    for team in standings:
        position = team['position']
        name = team['team']['name']
        points = team['points']
        print(f"{position}. {name} - {points} points")

def la_liga_results():
    url = "https://api.football-data.org/v4/competitions/PD/matches"
    api = os.getenv("football_api").strip()
    headers = {
        'X-Auth-Token': api
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    matches = data['matches']
    for match in matches:
        home_team = match['homeTeam']['name']
        away_team = match['awayTeam']['name']
        score_home = match['score']['fullTime']['home']
        score_away = match['score']['fullTime']['away']
        if score_home is None or score_away is None:
            continue
        print(f"{home_team} {score_home} - {score_away} {away_team}")

def la_liga_table():
    url = "https://api.football-data.org/v4/competitions/PD/standings"
    api = os.getenv("football_api").strip()
    headers = {
        'X-Auth-Token': api
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    standings = data['standings'][0]['table']
    for team in standings:
        position = team['position']
        name = team['team']['name']
        points = team['points']
        print(f"{position}. {name} - {points} points")

def ligue_results():
    url = "https://api.football-data.org/v4/competitions/FL1/matches"
    api = os.getenv("football_api").strip()
    headers = {
        'X-Auth-Token': api
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    matches = data['matches']
    for match in matches:
        home_team = match['homeTeam']['name']
        away_team = match['awayTeam']['name']
        score_home = match['score']['fullTime']['home']
        score_away = match['score']['fullTime']['away']
        if score_home is None or score_away is None:
            continue
        print(f"{home_team} {score_home} - {score_away} {away_team}")

def ligue_table():
    url = "https://api.football-data.org/v4/competitions/FL1/standings"
    api = os.getenv("football_api").strip()
    headers = {
        'X-Auth-Token': api
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    standings = data['standings'][0]['table']
    for team in standings:
        position = team['position']
        name = team['team']['name']
        points = team['points']
        print(f"{position}. {name} - {points} points")

