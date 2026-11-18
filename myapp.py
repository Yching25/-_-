import streamlit as st

st.set_page_config(page_title="My App", page_icon="🤍")

with st.sidebar:
    st.header("Setting")
    name = st.text_input("Your name", "Student")

st.title("BMI Calculator")
st.write("Move the sliders to enter your height and weight. "
         "Your BMI (Body Mass Index) updates instantly.")

col1, col2 = st.columns(2)
with col1:
    height_cm = st.slider("Height (cm)", 100, 220, 170)
with col2:
    weight_kg = st.slider("Weight (kg)", 30, 200, 65)

bmi = weight_kg / (height_cm / 100) ** 2

st.subheader(f"{name}'s result")
st.metric("Your BMI", f"{bmi:.1f}")

