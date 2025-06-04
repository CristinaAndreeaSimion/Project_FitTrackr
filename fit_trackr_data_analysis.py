import pandas as pd

# 1. Loading and knowing the data
df = pd.read_csv('fit_trackr_clean.csv')
# Removing rows without Username
df = df.dropna(subset=["Username"])

# 2. Data preprocessing
df["Duration_min"] = df["Duration"].str.replace(" min", "").astype(int)
df["Calories_kcal"] = df["Calories"].str.replace(" kcal", "").astype(float)

df["Activity"] = df["Activity"].str.lower().str.strip()
df["Activity"] = df["Activity"].replace({
    "swimm": "swimming",
    "run": "running",
    "walk": "walking",
    "cycle": "cycling"
})
df["Mood"] = df["Mood"].str.lower().str.strip().str.capitalize()

# Remove duplicate
df = df.drop_duplicates().reset_index(drop=True)

# 3. User Behavior Analysis

# 1. Average Activity Duration
mean_duration = df["Duration_min"].mean()

# 2. Most frequent activity
most_common_activity = df["Activity"].mode()[0]

#3. Most common mood
most_common_mood = df["Mood"].mode()[0]

# 4. Variation in calorie consumption depending on activity
calories_std_by_activity = df.groupby("Activity")["Calories_kcal"].std().sort_values(ascending=False)

# 5. Interquartile range (IQR) for user age
Q1 = df["Age"].quantile(0.25)
Q3 = df["Age"].quantile(0.75)
iqr_age = Q3 - Q1

# Display results
print("Average duration (minutes):", round(mean_duration, 2))
print("Frequent activity:", most_common_activity)
print("Frequent mood swings:", most_common_mood)
print("IQR Age of users:", iqr_age)
print("\nStandard deviation calories per activity:")
print(calories_std_by_activity)

# Save cleaned data
df.to_csv("fit_trackr_data_cleaned.csv", index=False)
