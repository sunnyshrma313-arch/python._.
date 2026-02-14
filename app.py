
import streamlit as st

# Page configuration
st.set_page_config(page_title="A Secret for You...", page_icon="💖")

# --- 1. MUSIC SECTION (I Wanna Be Yours - Arctic Monkeys) ---
st.write("### 🎵 Press Play & Feel the Vibe...")
# Stable YouTube link for 'I Wanna Be Yours'
audio_url = "https://www.youtube.com/watch?v=rf7Gv0m2S-g"
st.video(audio_url) 

# --- 2. HEADER ---
st.balloons() # FIXED: Brackets khali rakhein taaki error na aaye
st.title("Hey! Just wanted to say something... ✨")
st.markdown("---")

# --- 3. THE MESSAGE ---
st.header("Happy Valentine's Day! 🌹")
st.write("""
I was going to send a boring text, but then I thought—you deserve 
something built specially for you. You're the **Syntax** to my **Python**, 
the perfect logic in my chaotic code. 
""")

st.subheader("So... Will you be my Valentine? ❤️")

# --- 4. INTERACTIVE CHOICE ---
col1, col2 = st.columns(2)

with col1:
    if st.button('YES! 😍 (Recommended)'):
        st.balloons() # FIXED
        st.snow()     # FIXED: Brackets khali rakhein
        st.success("Best decision ever! ❤️ Check your WhatsApp now!")

with col2:
    if st.button('NO 😢 (Experimental)'):
        st.error("Error 404: 'No' option not found today! 😉")
        st.write("Try the other button, it's more stable!")

# --- 5. THE PERSONAL TOUCH ---
st.divider()
with st.expander("Click here to see 3 things I love about you:"):
    st.write("1. **Your Smile:** It's more beautiful than a perfect line of code.")
    st.write("2. **Your Energy:** You make everything better just by being there.")
    st.write("3. **Your Taste:** Because you're reading this right now. 😉")

# --- YOUR CUSTOM QUOTE & SIGNATURE (From your screenshot) ---
st.write("wish I was one of your tears. SO, I could be born in your eyes... run down to your cheek. And die on your lips....... 🥺😭")

st.markdown("PLEASE AB TO YES BOLDO YAAR DIMAG KHRAB HO GYA YE WEBSITE BANANE MAI ITNE EFFORTS LGAYE HAI AAPKE LIYE MUMMY KASAM KOI AI USE NAI HAI ISME AAP YES BOLDO MERA DIL KHUSH HO JAYEGA EK CHANCE DO AAP AAPKA DIL NAI TUTEGA")
st.write("Handcrafted with ❤️ and a lot of nerves aapki YES sunne k liye pagal AAPKA PYARA MASUM BACHA MANJOT 😊🤗🎀 .")
