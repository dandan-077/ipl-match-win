import streamlit as st
import pickle
import pandas as pd

# Load the RandomForest model
with open('random_forest_model.pkl', 'rb') as model_file:
    pipe = pickle.load(model_file)

# Define team mapping for 0 and 1 (assuming 0 is BowlingTeam and 1 is BattingTeam)
team_map = {
    0: 'Bowling Team',  # Change this to the actual name if needed
    1: 'Batting Team'   # Same for this, replace with your actual team names
}

# Streamlit App
st.title("IPL Match Prediction")

# Define the teams based on the provided list
teams = [
    'Delhi Capitals', 'Kolkata Knight Riders', 'Royal Challengers Bangalore', 
    'Mumbai Indians', 'Sunrisers Hyderabad', 'Rajasthan Royals', 
    'Punjab Kings', 'Chennai Super Kings', 'Gujarat Titans', 'Lucknow Super Giants'
]

# Define the cities based on the provided list
cities = [
    'Centurion', 'Johannesburg', 'Durban', 'Visakhapatnam', 'Chennai', 'Bangalore', 
    'Mumbai', 'Cape Town', 'Jaipur', 'Sharjah', 'Hyderabad', 'Ahmedabad', 'Bengaluru',
    'Navi Mumbai', 'Pune', 'Abu Dhabi', 'Cuttack', 'Chandigarh', 'Dubai', 'Kanpur', 
    'Rajkot', 'Raipur', 'Ranchi', 'Port Elizabeth', 'Indore', 'Bloemfontein', 'East London', 
    'Nagpur', 'Dharamsala', 'Kimberley'
]

# User Inputs
batting_team = st.selectbox("Select Batting Team", teams)
bowling_team = st.selectbox("Select Bowling Team", teams)
city = st.selectbox("Select City", cities)
runs_left = st.number_input("Runs Left", min_value=0)
balls_left = st.number_input("Balls Left", min_value=0)
wickets_left = st.number_input("Wickets Left", min_value=0)
current_run_rate = st.number_input("Current Run Rate", min_value=0.0)
required_run_rate = st.number_input("Required Run Rate", min_value=0.0)
target = st.number_input("Target", min_value=0)

# Prepare input data for prediction
input_data = pd.DataFrame({
    'BattingTeam': [batting_team],
    'BowlingTeam': [bowling_team],
    'City': [city],
    'runs_left': [runs_left],
    'balls_left': [balls_left],
    'wickets_left': [wickets_left],
    'current_run_rate': [current_run_rate],
    'required_run_rate': [required_run_rate],
    'target': [target]
})

# Predict button
if st.button("Predict Winning Team"):
    # Make prediction using the loaded model
    prediction = pipe.predict(input_data)
    
    # Map the predicted result to the actual team name
    winning_team = batting_team if prediction[0] == 1 else bowling_team
    
    # Display the result
    st.write(f"The predicted winning team is: {winning_team}")
