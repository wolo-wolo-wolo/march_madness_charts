import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

st.title('3PT Percentage and Opponent 3PT Percentage')

# Then, in any page, you can access it like so:
df = st.session_state['kenpom_df'][st.session_state['kenpom_df']['YEAR'] == 2024]

deep_df = df[['TEAM', 'SEED', '3PTR', '3PTRD']]

# Load the team IDs from CSV
team_ids_df = pd.read_csv('team_logo/logos/team_ids.csv')

# Assuming kenpom_df is your existing DataFrame and it's already defined
# Join kenpom_df with team_ids_df
# Assuming 'team' is the column in team_ids_df and 'TEAM' is the column in kenpom_df
merged_df = pd.merge(deep_df, team_ids_df, left_on='TEAM', right_on='team', how='left')

# Keep all columns from kenpom_df and the 'team id' from team_ids_df
# Assuming the column containing the team id in team_ids_df is named 'team id'
# If the column name is different, replace 'team id' with the correct column name
final_df = merged_df.drop(columns=['team']).dropna(subset=['team.id'])  # Drop the 'team' column from team_ids_df if not needed and filter out rows where 'team.id' is NaN


def getImage(path):
    return OffsetImage(plt.imread(path), zoom=0.025)  # Adjust zoom as needed

fig, ax = plt.subplots()
ax.scatter(final_df['3PTR'], final_df['3PTRD'], alpha=0)  # Plotting the points just for the layout

for index, row in final_df.iterrows():
    img_path = f"team_logo/logos/{int(row['team.id'])}.png"  # Adjust the path as necessary
    ab = AnnotationBbox(getImage(img_path), (row['3PTR'], row['3PTRD']), frameon=False)
    ax.add_artist(ab)

ax.set_xlabel('3 Point Make Percentage')
ax.set_ylabel('Opponent 3 Point Make Percentage')
ax.set_title('3PT Scatter Plot')
plt.gca().invert_yaxis()  # Invert Y-axis if needed

st.pyplot(fig)
