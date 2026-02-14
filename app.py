import streamlit as st

# Page configuration
st.set_page_config(page_title="A Secret for You...", page_icon="💖")

# --- 1. THE PERFECT ROMANTIC VIBE (Cute Valentine Jukebox) ---
st.write("### 🎵 Press Play & Feel the Love...")
# Specially curated Valentine's jukebox for a cute vibe
audio_url = "https://www.youtube.com/watch?v=Rdb5DnCTe9o" 
st.video(audio_url) 

# --- 2. HEADER (Fixed) ---
st.balloons() 
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
        st.balloons() 
        st.snow()     
        st.success("Best decision ever! ❤️ Check your WhatsApp now!")

with col2:
    if st.button('NO 😢 (Experimental)'):
        st.error("Error 404: 'No' option not found today! 😉")
        st.write("Python says: 'Please try the other button for better results.'")

# --- 5. THE PERSONAL TOUCH ---
st.divider()
with st.expander("Click here to see 3 things I love about you:"):
    st.write("1. **Your Smile:** It's more beautiful than a perfect line of code.")
    st.write("2. **Your Energy:** You make everything better just by being there.")
    st.write("3. **Your Taste:** Because you're reading this right now. 😉")

# --- YOUR CUSTOM QUOTE & SIGNATURE ---
st.write("wish I was one of your tears. SO, I could be born in your eyes... run down to your cheek. And die on your lips....... 🥺😭")

st.markdown("PLEASE AB TO YES BOLDO YAAR DIMAG KHRAB HO GYA YE WEBSITE BANANE MAI ITNE EFFORTS LGAYE HAI AAPKE LIYE MUMMY KASAM KOI AI USE NAI HAI ISME AAP YES BOLDO MERA DIL KHUSH HO JAYEGA EK CHANCE DO AAP AAPKA DIL NAI TUTEGA I JUST WANT A CHANCE MEREKO CHANCE DO LOYAL RHUNGA AAPKE LIYE😭😭🙏🏻")
st.write("Handcrafted with ❤️ and a lot of nerves aapki YES sunne k liye pagal AAPKA PYARA MASUM BACHA MANJOT 😊 .")
