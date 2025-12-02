import streamlit as st
import time

st.title("💊 Medicine Reminders")
st.write("Keep track of daily medication easily.")

meds = [
    "Vitamin D — Morning",
    "Blood Pressure Tablet — Evening",
    "Joint Pain Relief — Night"
]

completed = 0
for m in meds:
    if st.checkbox(m):
        completed += 1

# Show progress bar
progress = int((completed / len(meds)) * 100)
st.progress(progress)
st.info(f"{completed} of {len(meds)} medications completed.")

st.write("Voice assistant feature coming soon for reminders!")
