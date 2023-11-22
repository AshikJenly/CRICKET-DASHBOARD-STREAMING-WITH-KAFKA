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
    