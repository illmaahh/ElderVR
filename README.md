# 👵 ElderVR

**ElderVR** is an adaptive healthcare dashboard designed for elderly users. It features large fonts, simple navigation, health monitoring, medicine reminders, and relaxation tools. Built with Streamlit for an interactive, accessible experience.

## Features
- 🫀 Health Monitoring: Simulated heart rate, blood pressure, and pain score.
- 💊 Medicine Reminders: Simple checkboxes for medication schedules.
- 🌿 Stress Relief: Calming audio for relaxation.

## Screenshots
![Dashboard](screenshots/dashboard.png)
![Health Monitoring](screenshots/health.png)
![Medicine Reminders](screenshots/meds.png)
![Stress Relief](screenshots/relax.png)

## Run Locally
```bash
git clone https://github.com/illmaahh/ElderVR.git
cd ElderVR
python -m venv venv
source venv/bin/activate   # for Linux/Mac
venv\Scripts\activate      # for Windows
pip install -r requirements.txt
streamlit run app.py
