from .read_from_source import shared_data

match_id = -1

    
def get_team_details():
    if len(shared_data) != 0:
        data = shared_data[-1]
        teams = (data["batting_team"],data["bowling_team"])    
        return data["match_id"],teams   
    else:
        return None
     
def get_runs_per_over(team_name):
    runs = [data["total_runs"] for data in shared_data if data["batting_team"]==team_name]
    overs = [data["over"] for data in shared_data if data["batting_team"]==team_name]
    if len(runs) == 0:
        return []
    result = {}
    total_runs = 0

    for over, run in zip(overs, runs):
        total_runs += run
        result[over] = total_runs

    result_list = [result[key] for key in sorted(result.keys())]
    return result_list

def get_wickets_per_over(team_name):
    
    wickets = [data["player_dismissed"] for data in shared_data if data["batting_team"]==team_name and data["player_dismissed"]!="" and data["player_dismissed"] is not None]
    if len(wickets) == 0:
        return []
  
    return wickets

def get_batting_team():
    return shared_data[-1]["batting_team"]

def get_bowling_team():
    return shared_data[-1]["bowling_team"]
def get_batsmans_run(team_name,for_df = False):
    batsmans = [data["batsman"] for data in shared_data if data["batting_team"]==team_name]
    batsman_runs = {}
    
    for batsman in batsmans:
        runs = [data["batsman_runs"] for data in shared_data if data["batsman"]==batsman]
        batsman_runs[batsman] =runs
            
        
    return batsman_runs

def get_striker_and_n_s(team_name):
    try:
        data = shared_data[-1]
        striker = data["batsman"]
        non_striker = data["non_striker"]
        
        batsman_runs = get_batsmans_run(team_name)
        return (striker,batsman_runs[striker]),(non_striker,batsman_runs[non_striker])
    except KeyError:
        return None

def get_balls_faced(player_name,batsman=True):
    if batsman:
        balls = sum(1 for data in shared_data if data["batsman"] == player_name)
        return balls
    else:
        balls = sum(1 for data in shared_data if data["bowler"] == player_name)
        return balls
def get_wickets(player_name):
    wickets = sum(1 for data in shared_data if data["bowler"] == player_name and len(data["player_dismissed"]) !=0 )
    return wickets
def get_bowler():
    return shared_data[-1]["bowler"]

def get_batsman_history(team_name):
    batsmans = set([data["batsman"] for data in shared_data if data["batting_team"]==team_name])
    
    data = {"BatsMan":[],"Runs":[]}
    for batsman in batsmans:
        # print(batsman)
        data["BatsMan"].append(batsman)
        data["Runs"].append(sum(get_batsmans_run(team_name)[batsman]))
    return data