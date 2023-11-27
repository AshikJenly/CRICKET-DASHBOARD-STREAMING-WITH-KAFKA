import streamlit as st
import pandas as pd
import numpy as np
import time

from source.process_data import (
    get_team_details,
    get_runs_per_over,
    get_wickets_per_over,
    get_striker_and_n_s,
    get_batting_team,
    get_bowler,
    get_balls_faced,
    get_bowling_team,
    get_wickets,
    get_bowling_history,
    get_batsman_history
    )
from itertools import zip_longest

st.set_page_config(layout="wide")

team_details = get_team_details()
title = st.empty()
Team_A,Team_B = None,None
team = st.empty()
st.markdown("<hr style='border:2px solid white'>", unsafe_allow_html=True)

batting, bowling = st.columns(2)

with batting:
    batting_team = st.empty()
    ba1 = st.empty()
    ba2 = st.empty()

# Add content to the second column
with bowling:
    bowling_team = st.empty()
    bowler = st.empty()
st.markdown("<hr style='border:2px solid white'>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align:center'>Score Graph 📈</h3>", unsafe_allow_html=True)
line_chart = st.empty()

# ----------------- HISTORY -------------------
st.title("History")
batting_history_1,bowling_history_1 = st.columns(2)
batting_history_2,bowling_history_2 = st.columns(2)

with batting_history_1:
    bat_table_1_h = st.empty()
    bat_table_1 = st.empty()
with batting_history_2:
    bat_table_2_h = st.empty()
    bat_table_2 = st.empty()
with bowling_history_1:
    bow_history_1_h = st.empty()
    bow_history_1 = st.empty()
with bowling_history_2:
    bow_history_2_h = st.empty()
    bow_history_2 = st.empty()
      
Team_A_run = st.empty()
Team_B_run = st.empty()

try:
    while True:
        team_details = get_team_details()

        if team_details is not None:
            if Team_A is None:
                
                Team_A = team_details[1][0]
                Team_B = team_details[1][1]
                bat_table_1_h.markdown("<h4>"+Team_A+"Batting Score"+"</h4>",unsafe_allow_html=True)
                bat_table_2_h.markdown("<h4>"+Team_B+"</h4>",unsafe_allow_html=True)
                bow_history_1_h.markdown("<h4>"+Team_B+"</h4>",unsafe_allow_html=True)
                bow_history_2_h.markdown("<h4>"+Team_A+"</h4>",unsafe_allow_html=True)
            team.markdown(f"<h1 style='text-align:center'>{Team_A}  vs {Team_B}</h1>",unsafe_allow_html=True)

            # batting.write(f"Batting Score of {Team_A}")
            team_a_runs = get_runs_per_over(Team_A)
            team_b_runs = get_runs_per_over(Team_B)
            a_wickets = get_wickets_per_over(Team_A)
            b_wickets = get_wickets_per_over(Team_B)

            # Pad the shorter list with np.nan
            # if team_b_runs is not None:
            padded_data = list(zip_longest(team_a_runs, team_b_runs,[None for i in range(0,21 )], fillvalue=None))
            x_padded, y_padded ,_= zip(*padded_data)
            team_a_runs_padded = list(x_padded)
            team_b_runs_padded = list(y_padded)

            # Batting Details
            # try:
            batting_team.markdown(
                f"<span style='font-size: 30px;'>🏏 {get_batting_team()} : {team_a_runs[-1]}/{len(a_wickets)}\t({len(team_a_runs)})</span>",
                unsafe_allow_html=True
                )


        
            striker, non_striker = get_striker_and_n_s(get_batting_team())
            ba1.write(f"{striker[0]} - {sum(striker[1])} ({get_balls_faced(striker[0])} balls) *")
            ba2.write(f"{non_striker[0]} - {sum(non_striker[1])} ({get_balls_faced(non_striker[0])} balls)")
            bowler.write(f"{get_bowler()} - {get_wickets(get_bowler())}/{get_balls_faced(get_bowler(),batsman=False)}")
           


            # ---------- HISTORY --------------------
            bat_table_1.table(pd.DataFrame(get_batsman_history(Team_A)))
            bat_table_2.table(pd.DataFrame(get_batsman_history(Team_B)))
            bow_history_1.table(pd.DataFrame(get_bowling_history(Team_B)))
            bow_history_2.table(pd.DataFrame(get_bowling_history(Team_A)))
                        
            #----------------------------------------
            Team_A_run.write(
                f"{Team_A} : {team_a_runs[-1]}/{len(a_wickets)}\t({len(team_a_runs)})")
            if len(team_b_runs) != 0:
                Team_B_run.write(f"{Team_B} :{team_b_runs[-1]}/{len(b_wickets)}\t({len(team_b_runs)})")
                bowling_team.markdown(
                f"<span style='font-size: 30px;'>⚾ {get_bowling_team()} : {team_b_runs[-1]}/{len(b_wickets)}\t({len(team_b_runs)})</span>",
                unsafe_allow_html=True
                )
            else:
                Team_B_run.write(f"{Team_B} : Not Yet Batted")
            df = pd.DataFrame({
                Team_A: team_a_runs_padded,
                Team_B: team_b_runs_padded,
            })
            # Plot the lines
            line_chart.line_chart(df, use_container_width=True)
            time.sleep(2)
            title.title("JEN.live")

        else:
            title.title("Loading Please Wait")
            title.markdown("<style>h1 {text-align: center;}</style>", unsafe_allow_html=True)

except TypeError:
    pass
