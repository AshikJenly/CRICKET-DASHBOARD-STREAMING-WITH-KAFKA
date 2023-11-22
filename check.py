# from source.process_data import get_team_details,get_runs_per_over
# import pandas as pd
# import time
# team_details = get_team_details()
# try:
#     while True:
#         team_details = get_team_details()
        
#         if team_details is not None:
#             print("Printing")
#             batting_team = team_details[1][0]
#             bowling_team = team_details[1][1]
            
#             runs = get_runs_per_over(batting_team)
#             runs_2 = get_runs_per_over(bowling_team)
#             data = {
#                 'x':[i for i in range(0,len(runs))-1],
#                 'A':runs,
#                 'B':runs_2
#             }
#             df = pd.DataFrame(data)
#             print(df)
#         time.sleep(3)
# except TypeError:
#     pass

import streamlit as st
import pandas as pd
import numpy as np

# Sample data with different lengths
data = {
    'x': [1, 2, 3, 4, 5],
    'line1': [10, 15, 13, 17, 20],  # Line 1 data
    'line2': [5, 8, 12, 10],        # Line 2 data (different length)
}

# Find the maximum length
max_len = max(len(data['line1']), len(data['line2']))

# Fill missing values with NaN
for key in data:
    data[key] += [np.nan] * (max_len - len(data[key]))

# Convert data to DataFrame
df = pd.DataFrame(data)

# Plot the lines
st.line_chart(df.set_index('x'))
