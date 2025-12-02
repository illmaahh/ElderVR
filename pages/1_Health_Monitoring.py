import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title("🫀 Health Monitoring")
st.write("Live health statistics simulated for demonstration.")

# Simulate health data
time = pd.date_range('2025-12-01', periods=10)
heart_rate = np.random.randint(70, 90, size=10)
blood_pressure = np.random.randint(110, 130, size=10)

df = pd.DataFrame({
    'Time': time,
    'Heart Rate (bpm)': heart_rate,
    'Blood Pressure (mmHg)': blood_pressure
})

# Line chart for heart rate
st.subheader("Heart Rate Over Time")
st.line_chart(df.set_index('Time')['Heart Rate (bpm)'])

# Line chart for blood pressure
st.subheader("Blood Pressure Over Time")
st.line_chart(df.set_index('Time')['Blood Pressure (mmHg)'])

# Current metrics
st.metric("Current Heart Rate", f"{heart_rate[-1]} bpm", f"{heart_rate[-1]-heart_rate[-2]} change")
st.metric("Current Blood Pressure", f"{blood_pressure[-1]} mmHg", f"{blood_pressure[-1]-blood_pressure[-2]} change")
st.metric("Pain Score", f"{np.random.randint(0,5)}/10", "Comfort improving")
