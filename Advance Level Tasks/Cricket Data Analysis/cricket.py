import pandas as pd
import random

weights = {
    'Clean Pick': 1,
    'Good Throw': 2,
    'Catch': 3,
    'Dropped Catch': -3,
    'Stumping': 2,
    'Run Out': 5,
    'Missed Run Out': -2,
    'Direct Hit': 4,
    'Runs Saved': 1
}

players = ["Virat Kohli", "Ravindra Jadeja", "Steve Smith", "Ben Stokes", "Glenn Maxwell"]
positions = ["Slip", "Point", "Covers", "Mid-on", "Mid-off", "Square Leg"]
picks = list(weights.keys())[:-1]
throws = ["Run Out", "Missed Run Out", "Stumping", "Direct Hit", "None"]

data = []
for i in range(1, 101):
    player = random.choice(players)
    position = random.choice(positions)
    pick = random.choice(picks)
    throw = random.choice(throws)
    runs = random.randint(-3, 5)
    
    data.append([i, player, position, pick, throw, runs])

columns = ["Event ID", "Player Name", "Position", "Pick", "Throw", "Runs"]
df = pd.DataFrame(data, columns=columns)

df["Pick Score"] = df["Pick"].map(weights).fillna(0)
df["Throw Score"] = df["Throw"].map(weights).fillna(0)
df["Runs Score"] = df["Runs"] * weights["Runs Saved"]

df["Performance Score"] = df["Pick Score"] + df["Throw Score"] + df["Runs Score"]

performance_summary = df.groupby("Player Name", as_index=False)["Performance Score"].sum()

print(performance_summary)

performance_summary.to_csv("fielding_performance_analysis.csv", index=False)
