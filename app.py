import streamlit as st

# Page configuration - Isse website ka naam aur icon set hota hai
st.set_page_config(page_title="A Secret for You...", page_icon="💖")

# --- 1. THE VIBE (Music) ---
st.write("### 🎵 Press Play & Feel the Vibe...")
# Direct link to Golden Brown (hope this one stays live!)
audio_url = "https://www.soundboard.com/handler/DownLoadTrack.ashx?cliptoken=55227092-2391-4e45-8b17-062e49c7161b"
st.audio(audio_url)

# --- 2. THE OPENING ---
st.balloons()
st.title("Hey! Just wanted to say something... ✨")
st.markdown("---")

# --- 3. THE HEART OF THE MATTER ---
st.header("Happy Valentine's Day! 🌹")
st.write("""
I was going to send a boring text, but then I thought—you deserve 
something built specially for you. You're the **Syntax** to my **Python**, 
the perfect logic in my chaotic code. 
""")

st.subheader("So... Will you be my Valentine? ❤️")

# --- 4. THE INTERACTIVE CHOICE ---
col1, col2 = st.columns(2)

with col1:
    if st.button('YES! 😍 (Recommended)'):
        st.balloons()
        st.snow()
        st.success("Best decision ever! You just made me the happiest person! ❤️")
        st.confetti() # Agar ye kaam na kare toh balloons toh hai hi!
        st.write("### Ab jaldi se instagram par message karo! 📱")

with col2:
    if st.button('NO 😢 (Experimental)'):
        # Yeh button "No" nahi hone dega
        st.error("Error 404: 'No' is not a valid input today! ❌")
        st.write("Python says: 'Please try the other button for better results.' 😉")

# --- 5. THE PERSONAL TOUCH ---
st.divider()
with st.expander("Click here to see 3 things I love about you:"):
    # Yahan apni baatein likho!
    st.write("1. **Your Smile:** It's more beautiful than a perfect line of code.")
    st.write("2. **Your Energy:** You make everything better just by being there.")
    st.write("3. **Your Taste:** Because you're reading this right now. 😉")

st.markdown(" wish I was one of your tears. SO, I could be born in your eyes... run down to your cheek. And die on your lips....... 😖")
st.caption("Handcrafted with ❤️ and a lot of nerves aapki YES sunne k liye pagal AAPKA PYARA MASUM BACHA MANJOT 😊🤗.")
