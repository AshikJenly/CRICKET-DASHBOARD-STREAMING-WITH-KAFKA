import streamlit as st
from source.process_data import get_team_details,get_runs_per_over
#Heading
team_details = get_team_details()
try:
    batting_team = team_details[1][0]
    bowling_team = team_details[1][1]
    st.title(f"Match No : {team_details[0]}")
    st.title(f"{batting_team}  vs {bowling_team}")



    #Batting Team
    st.write(f"Batting Score of {batting_team}")

    runs = get_runs_per_over(batting_team)
    st.line_chart(runs)
except TypeError:
    pass