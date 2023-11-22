import streamlit as st
import pandas as pd
import numpy as np
from source.process_data import get_team_details, get_runs_per_over

# Heading
import time

team_details = get_team_details()
title = st.empty()
team = st.empty()
batting = st.empty()
info = st.empty()
line_chart = st.empty()

try:
    while True:
        team_details = get_team_details()

        if team_details is not None:

            batting_team = team_details[1][0]
            bowling_team = team_details[1][1]
            title.title(f"Match No : {team_details[0]}")
            team.title(f"{batting_team}  vs {bowling_team}")

            batting.write(f"Batting Score of {batting_team}")
            # Batting Team
            runs = get_runs_per_over(batting_team)
            runs_2 = get_runs_per_over(bowling_team)

            x = [i for i in range(0, min(len(runs), len(runs_2)))]

            info.write(
                f"{batting_team} : {runs[-1]}/{len(runs)} \t {bowling_team} :{runs_2[-1]}/{len(runs_2)}")

            # Plot the lines
            line_chart.line_chart({
                'A': runs[:len(x)],
                'B': runs_2[:len(x)],
            }, use_container_width=True)

            # If you want to use a DataFrame:
            # data = {'x': x, 'A': runs[:len(x)], 'B': runs_2[:len(x)]}
            # df = pd.DataFrame(data)
            # line_chart.line_chart(df.set_index('x'), use_container_width=True)

        else:
            title.title("Loading Please Wait")
except TypeError:
    pass
