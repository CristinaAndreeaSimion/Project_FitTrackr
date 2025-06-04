import pandas as pd

df = pd.read_csv('fit_trackr_clean.csv')

# Removing rows without Username
df = df.dropna(subset=["Username"])

# Column cleaning and transformation
df["Duration_min"] = df["Duration"].str.replace(" min", "").astype(int)
df["Calories_kcal"] = df["Calories"].str.replace(" kcal", "").astype(float)

# Standardization of activity names and moods
df["Activity"] = df["Activity"].str.lower().str.strip().replace({
    "swimm": "swimming",
    "run": "running",
    "walk": "walking",
    "cycle": "cycling"
})
df["Mood"] = df["Mood"].str.lower().str.strip().str.capitalize()

# Remove duplicates
df = df.drop_duplicates().reset_index(drop=True)

# Save cleaned data
df.to_csv("fit_trackr_data_cleaned.csv", index=False)
