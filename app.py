import streamlit as st

# Page config
st.set_page_config(
    page_title="ElderVR",
    page_icon="👵",
    layout="wide"
)

# Custom CSS for large fonts & buttons
st.markdown("""
    <style>
    body {font-size: 20px; line-height: 1.6;}
    .stButton>button {font-size: 22px; padding: 15px;}
    .css-18e3th9 {padding: 25px 20px;}
    </style>
""", unsafe_allow_html=True)

# Title and welcome text
st.title("👵 Welcome to ElderVR")
st.subheader("An adaptive healthcare dashboard designed for elderly users.")
st.write("""
Click the sidebar to explore **Health Monitoring**, **Medicine Reminders**, and **Stress Relief** tools.
""")

# Add an image or GIF
st.image(
    "https://images.unsplash.com/photo-1576765607928-7f1efde6505f?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8ZWxkZXJseSUyMGhlYWx0aHxlbnwwfHwwfHw%3D&ixlib=rb-4.0.3&q=80",
    caption="Healthy and happy elderly users",
    use_container_width=True
)

# Mode selection
mode = st.radio("Choose Display Mode:", ["Normal View", "Senior Comfort Mode"])

if mode == "Senior Comfort Mode":
    st.markdown("""
        <style>
        body { font-size: 24px; line-height: 1.8; }
        .stButton>button { font-size: 26px; padding: 20px; }
        </style>
    """, unsafe_allow_html=True)

st.success("Use the sidebar to navigate between panels.")
