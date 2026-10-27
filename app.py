import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Good Luck for Your Interview! 🚀",
    page_icon="🍀",
    layout="centered"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main-title {
        font-size: 2.8rem;
        color: #1E3A8A;
        text-align: center;
        font-weight: bold;
    }
    .sub-title {
        font-size: 1.5rem;
        color: #4B5563;
        text-align: center;
    }
    .card {
        background-color: #F3F4F6;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Trigger celebration animations automatically when the page loads
st.balloons()

# Main Header
st.markdown('<p class="main-title">🍀 Good Luck, Monkeyyy! 🚀</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Go crush that interview tomorrow!</p>', unsafe_allow_html=True)

st.write("---")

# Fun motivational quote / message section
st.markdown("""
<div class="card">
    <h3>You've got this! 💪</h3>
    <p>All the preparation, late nights, and hard work lead up to this moment. 
    Take a deep breath, trust your skills, and show them how awesome you are!</p>
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("### Tap an icon for a sneak peek! ✨")

# Interactive Icon Buttons stacked vertically
if st.button("📄 Offer Letter Status"):
    st.balloons()
    st.success("Status: **Offer Letter Coming Soon!** 🥂")

if st.button("🌆 Next Stop"):
    st.snow()
    st.info("Status: **BLR Chapter Loading...** Get ready! 🎒✈️")

# Footer
st.write("")
st.markdown(
    "<p style='text-align: center; color: #9CA3AF; font-size: 0.9rem;'>Made with 💙 just for your big day.</p>", 
    unsafe_allow_html=True
)