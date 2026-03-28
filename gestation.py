import streamlit as st
import datetime
from datetime import timedelta

st.title("Pregnancy Calculator")

# 1. Use quotes for the label
# 2. Assign default value to avoid issues on first load
LMP = st.date_input(
    "Enter your first date of your last menstrual period (YYYY-MM-DD):",
    value=datetime.date.today()
)

# Define todays_date
todays_date = datetime.date.today()

# Check if LMP is not in the future
if LMP > todays_date:
    st.error("Error: LMP cannot be in the future.")
else:
    # Correct calculation: Extract .days from the timedelta result
    days_pregnant = (todays_date - LMP).days
    Age_of_Foetus = 0
    Age_of_Foetus = days_pregnant / 7
    
    due_date = LMP + timedelta(days=280)
    
    st.write(f"Gestational Age: {days_pregnant} days ({round(Age_of_Foetus, 1)} weeks)")
    st.write(f"Estimated Due Date: {due_date}")