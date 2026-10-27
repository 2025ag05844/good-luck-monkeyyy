import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Good Luck for Your Interview! 🚀",
    page_icon="🍀",
    layout="centered"
)

# Custom CSS to fix text colors and make the card look great in dark/light mode
st.markdown("""
    <style>
    .main-title {
        font-size: 2.8rem;
        color: #38BDF8;
        text-align: center;
        font-weight: bold;
    }
    .sub-title {
        font-size: 1.5rem;
        color: #9CA3AF;
        text-align: center;
    }
    .card {
        background-color: #1E293B;
        padding: 25px;
        border-radius: 12px;
        text-align: center;
        margin-top: 20px;
        border: 1px solid #334155;
    }
    .card h3 {
        color: #F8FAFC;
        margin-bottom: 10px;
    }
    .card p {
        color: #CBD5E1;
        font-size: 1.1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Trigger celebration animations automatically when the page loads
st.balloons()

# Main Header
st.markdown('<p class="main-title">🍀 Good Luck, Monkeyyy! 🚀</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Go crush that interview tomorrow!</p>', unsafe_allow_html=True)

st.write("---")

# Fun motivational quote / message section with high-contrast text
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
