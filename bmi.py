import streamlit as st
# from PIL import Image
# App title
st.title("Gestational Age Calculator")
# Display image
# image = Image.open("bmi_image.png")
# st.image(image, caption="Body Mass Index Illustration",
# use_container_width=True)
# Input fields
from datetime import date
todays_date = date.today()
print(todays_date)

name = st.text_input("Enter your name:")
LMP = st.date_input("Enter your first date of your last menstrual period (YYYY-MM-DD):")
# weight = st.number_input("Enter your weight (in kg):", format="%.2f")
# Calculate Gestational Age in weeks
if st.button("Calculate Gestational Age in weeks (Note: Baby is normally born at 40 weeks)"):
    Age_of_Foetus = (todaysDate - LMP) / 7
    
    st.success(f"{name}, the gestational age of your unborn baby is {Age_of_Foetus}, and the expected date of delivery is date{LMP+280}")

else:
    st.error("Please enter a valid LMP date.")