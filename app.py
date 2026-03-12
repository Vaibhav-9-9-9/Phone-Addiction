import pandas as pd 
import numpy as np 
import streamlit as st 
import pickle 

with open('phone.pkl','rb') as f:
    model=pickle.load(f)


st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://media.gettyimages.com/id/537460890/photo/teenager-sending-email-from-smart-phone-in-her-bed.jpg?s=612x612&w=0&k=20&c=oHJD6aekNxpJv91QM9KsGkNsJkFPTtEp4lzJ5nrtd-k=");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.title("Phone Addiction Prediction")

if st.toggle("Start Prediction"):

    age = st.number_input("Enter Age",0)

    gender = st.pills("Gender",["Male","Female","Other"])

    location = st.text_input("Enter Location")

    daily_usage_hours = st.slider("Enter Daily Usage Hours Of Phone",
        0.0, 24.0,
        value=0.0,
        step=0.1,
        format="%.1f")

    sleep_hours = st.slider("Enter Sleep Hours",
        0.0, 24.0,
        value=0.0,
        step=0.1,
        format="%.1f")

    interllectual_score = st.number_input("Enter Interllectual Performance",0)

    interactions = st.slider("Enter Social Interactions Per Day",
        0, 20,
        value=0,
        step=1)

    exercise_hours = st.slider("Enter Exercise Hours",
        0.0, 5.0,
        value=0.0,
        step=0.1,
        format="%.1f")

    anxiety_level = st.selectbox("Anxiety Level",list(range(11)))
    depression_level = st.selectbox("Depression Level",list(range(11)))
    esteem_level = st.selectbox("Self Esteem Level",list(range(11)))

    screen_time_before_bed = st.slider("Screen Time Before Bed",
        0.0, 5.0,
        value=0.0,
        step=0.1,
        format="%.1f")

    phone_checks_per_day = st.number_input("Phone Checks Per Day",0)

    apps_used_daily = st.selectbox("Apps Used Daily",list(range(31)))

    time_on_social_media = st.slider("Enter Time On Social Media",
        0.0, 5.0,
        value=0.0,
        step=0.1,
        format="%.1f")

    time_on_gaming = st.slider("Enter Time On Gaming",
        0.0, 5.0,
        value=0.0,
        step=0.1,
        format="%.1f")

    time_on_education = st.slider("Enter Time On Education",
        0.0, 5.0,
        value=0.0,
        step=0.1,
        format="%.1f")

    phone_usage_purpose = st.selectbox("Enter Phone Usage Purpose",['Browsing', 'Education', 'Social Media', 'Gaming', 'Other'])

    family_communication = st.selectbox("Family Communication",list(range(11)))

    weekend_usage_hours = st.slider("Enter Weekend Usage Hours Of Phone",
        0.0, 24.0,
        value=0.0,
        step=0.1,
        format="%.1f")

    if st.button("Predict Addiction Level"):
        input_df = pd.DataFrame([{
                "Age" : age,
                "Gender" : gender,
                "Location" : location,
                "Daily_Usage_Hours" : daily_usage_hours,
                "Sleep_Hours" : sleep_hours,
                "Interllectual_Performance" : interllectual_score,
                "Social_Interactions" : interactions,
                "Exercise_Hours" : exercise_hours,
                "Anxiety_Level": anxiety_level,
                "Depression_Level" : depression_level,
                "Self_Esteem" : esteem_level,
                "Screen_Time_Before_Bed" : screen_time_before_bed,
                "Phone_Checks_Per_Day" : phone_checks_per_day,
                "Apps_Used_Daily" : apps_used_daily,
                "Time_on_Social_Media" : time_on_social_media,
                "Time_on_Gaming" : time_on_gaming,
                "Time_on_Education" : time_on_education,
                "Phone_Usage_Purpose" : phone_usage_purpose,
                "Family_Communication" : family_communication,
                "Weekend_Usage_Hours" : weekend_usage_hours
                }])

        result = model.predict(input_df)[0]
        st.success(f"Predicted Addiction Level : {result:.1f}")

fb = st.feedback("thumbs")

if fb == "up":
    st.success("Thanks for your feedback! 👍")
elif fb == "down":
    st.warning("Thanks! We'll work on improving the model 👎")

    
