import streamlit as st
import pandas as pd

# Page title
st.title("Which feature should PantryPal build first?")

# The criteria and how much each one counts (they add up to 100)
weights = {
    "User impact": 30,
    "Less waste": 25,
    "Ease to build": 20,
    "Revenue": 15,
    "Confidence": 10,
}

# Starting scores for each feature (1 = weak, 5 = strong)
data = {
    "Feature": ["Expiry alerts", "Receipt scanning", "Recipe ideas", "Shared shopping list", "Barcode scanner"],
    "User impact": [5, 4, 4, 3, 3],
    "Less waste": [5, 3, 4, 2, 3],
    "Ease to build": [4, 2, 3, 4, 3],
    "Revenue": [2, 3, 4, 2, 2],
    "Confidence": [4, 3, 2, 3, 4],
}

table = pd.DataFrame(data)

# Show the table so people can change the scores
table = st.data_editor(table, hide_index=True, disabled=["Feature"])

# Work out the score for each feature
scores = {}

for i in range(len(table)):
    feature = table["Feature"][i]
    total = 0

    for criterion in weights:
        score = table[criterion][i]
        total = total + score * weights[criterion]

    scores[feature] = total / 100

# Sort from highest to lowest score
ranked = sorted(scores.items(), key=lambda item: item[1], reverse=True)

# Show the scoreboard
st.header("Scoreboard")

position = 1
for feature, score in ranked:
    st.write(f"**{position}. {feature}**: {score:.2f}")
    st.progress(min(score / 5, 1.0))
    position = position + 1

# Show the winner
winner = ranked[0][0]
st.subheader(f"Build {winner} first!")
