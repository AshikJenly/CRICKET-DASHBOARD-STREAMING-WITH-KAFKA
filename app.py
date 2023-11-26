import streamlit as st
import pandas as pd
import numpy as np
from source.process_data import get_team_details, get_runs_per_over,get_wickets_per_over
from itertools import zip_longest

# Heading
import time

team_details = get_team_details()
title = st.empty()
team = st.empty()

col1, col2 = st.columns(2)
with col1:
    c1_h = st.empty()
    c1_h.header("Column 1")
    st.text("Content for column 1")

# Add content to the second column
with col2:
    c2_h = st.empty()
    c2_h.header("Column 2")
    st.text("Content for column 2")

Team_A_run = st.empty()
Team_B_run = st.empty()
line_chart = st.empty()

# batsman
# Create a 2-column layout

# Add content to the first column


try:
    while True:
        team_details = get_team_details()

        if team_details is not None:

            Team_A = team_details[1][0]
            Team_B = team_details[1][1]
            title.title(f"Match No : {team_details[0]}")
            team.title(f"{Team_A}  vs {Team_B}")

            # batting.write(f"Batting Score of {Team_A}")
            runs = get_runs_per_over(Team_A)
            runs_2 = get_runs_per_over(Team_B)
            a_wickets = get_wickets_per_over(Team_A)
            b_wickets = get_wickets_per_over(Team_B)
    
            # Pad the shorter list with np.nan
            # if runs_2 is not None:
            padded_data = list(zip_longest(runs, runs_2, fillvalue=None))
            x_padded, y_padded = zip(*padded_data)
            runs_padded = list(x_padded)
            runs_2_padded = list(y_padded)
            
            c1_h.header(Team_A)
            c2_h.header(Team_B)
            Team_A_run.write(
                f"{Team_A} : {runs[-1]}/{len(a_wickets)}\t({len(runs)})")
            if len(runs_2)!=0:
                Team_B_run.write(f"{Team_B} :{runs_2[-1]}/{len(b_wickets)}\t({len(runs_2)})")
            else:
                Team_B_run.write(f"{Team_B} : Not Yet Batted")
            df = pd.DataFrame({
                Team_A: runs_padded,
                Team_B: runs_2_padded,
            })
            # Plot the lines
            line_chart.line_chart(df, use_container_width=True)
            time.sleep(2)
        else:
            title.title("Loading Please Wait")
except TypeError:
    pass
