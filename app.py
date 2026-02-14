import streamlit as st

# Page setup
st.set_page_config(page_title="For Someone Special ❤️", page_icon="🌹")

# --- MUSIC SECTION (Direct MP3 Link) ---
st.write("🎵 **Listen to this while reading:**")
# Golden Brown direct audio link
audio_file = "https://youtu.be/AWAsI3U2EaE?si=tHDFlkghO1erMhI_"
st.audio(audio_file)

# --- HEADER ---
st.balloons()
st.title("Hey! I have something to tell you... ✨")

# --- THE MESSAGE ---
st.header("Happy Valentine's Day! 🌹")
st.write("""
I've been thinking about how to say this for a while, but I thought 
coding it would be more 'me'. From our chats to the way 
you make me smile, everything about you is special.
""")

st.subheader("Will you be my Valentine? ❤️")

# --- INTERACTIVE BUTTONS ---
col1, col2 = st.columns(2)

with col1:
    if st.button('YES! 😍'):
        st.balloons()
        st.snow()
        st.success("Yay! You just made my day! ❤️")
        st.write("Ab jaldi se INSTAGRAM pr 'YES' likh kr bhejo!! 📱")

with col2:
    if st.button('NO 😢'):
        st.warning("Oops! This button is broken today. Try the left one! 😉")

# --- A CUTE LIST ---
st.divider()
with st.expander("3 Reasons why I like you:"):
    st.write("1. Your vibe is unmatched (just like this song).")
    st.write("2. You have the most amazing smile.")
    st.write("3. You make everything better just by being there.")

st.markdown("---")
st.caption("Made with ❤️ by your favorite coder and aapki YES sunne k liye pagal aapka PYARA BACHA MANJOT.")
