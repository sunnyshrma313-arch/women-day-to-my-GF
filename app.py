import streamlit as st

# Page setup for a clean look
st.set_page_config(page_title="For You", page_icon="✨")

# --- HEADER ---
st.title("Just for you... ✨")
st.markdown("---")

# --- THE MESSAGE ---
st.header("Happy International Women's Day! 🌹")
st.write("""
Aaj ka din tumhare liye hai. Waise toh tumhare liye har din special hai, 
par aaj main bas ye kehna chahta hoon ki tumhari presence meri life mein 
kisi magic se kam nahi hai.
""")

st.write("""
aapki samajh, aapki muskaan, aur aapka mere saath hona—ye sab cheezein 
mere liye duniya mein sabse zyada maayne rakhti hain. 
""")

# --- INTERACTIVE BUTTON ---
st.subheader("Ek chota sa surprise?")

if st.button("Click here 🎁"):
    st.balloons()
    st.success("Thank you for being you. You make the world (and my life) a better place! ❤️")

# --- PERSONAL QUOTE ---
st.divider()
st.write("*'In your eyes, I found my home. In your heart, I found my world.'*")

st.markdown("With you, love feels effortless and infinite.")
st.caption("With love, from yours truly.")
